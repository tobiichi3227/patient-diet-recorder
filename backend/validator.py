import re
from datetime import date, datetime
from datetime import time as time_cls
from typing import Any

from pydantic import (
    BaseModel,
    Field,
    NonNegativeInt,
    RootModel,
    model_validator,
)


def parse_date_key(key: str) -> date:
    try:
        y, m, d = map(int, key.split("_"))
        return date(y, m, d)
    except Exception as e:
        raise ValueError(e) from e


def parse_record_date(value: str) -> date:
    try:
        m, d = map(int, value.split("/"))
        return date.today().replace(month=m, day=d)
    except Exception as e:
        raise ValueError(e) from e


def parse_time(value: str) -> time_cls:
    try:
        return datetime.strptime(value, "%H:%M").time()
    except Exception as e:
        raise ValueError(e) from e


class RecordItem(BaseModel):
    time: str
    food: NonNegativeInt
    water: NonNegativeInt
    urination: NonNegativeInt
    defecation: NonNegativeInt


class DailyRecord(BaseModel):
    data: list[RecordItem]
    count: NonNegativeInt
    recordDate: str
    foodSum: NonNegativeInt
    waterSum: NonNegativeInt
    urinationSum: NonNegativeInt
    defecationSum: NonNegativeInt
    weight: str

    @model_validator(mode="after")
    def validate_all(self):
        if self.count != len(self.data):
            raise ValueError("count does not match data length")

        for field in ["food", "water", "urination", "defecation"]:
            expected = sum(getattr(item, field) for item in self.data)
            actual = getattr(self, f"{field}Sum")
            if actual != expected:
                raise ValueError(
                    f"{field}Sum expected {expected}, got {actual}"
                )

            if not isinstance(actual, int):
                raise ValueError

        record_date = parse_record_date(self.recordDate)
        if record_date > date.today():
            raise ValueError(f"recordDate is in the future: {self.recordDate}")

        if self.weight != "NaN":
            if not re.fullmatch(r"(-?\d+(?:\.\d+))? kg", self.weight):
                raise ValueError(f"invalid weight format: {self.weight}")
            weight_val = float(self.weight.split()[0])
            if weight_val <= 0:
                raise ValueError("weight must be a positive integer")

        for record in self.data:
            if record_date < date.today():
                continue
            input_time = parse_time(record.time)
            now = datetime.now().time()
            if input_time > now:
                raise ValueError(f"time {input_time} is in the future")

        return self


class PatientData(BaseModel):
    isEditing: bool
    limitAmount: str
    foodCheckboxChecked: bool
    waterCheckboxChecked: bool
    records: dict[str, DailyRecord] = Field(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def split_records(cls, values: dict[str, Any]):
        values = values.copy()
        reserved = {
            "isEditing",
            "limitAmount",
            "foodCheckboxChecked",
            "waterCheckboxChecked",
        }
        records = {k: v for k, v in values.items() if k not in reserved}

        values["records"] = records

        for key in records:
            if parse_date_key(key) > date.today():
                raise ValueError(f"record key {key} is in the future")

        return values


class UpdateDataModel(RootModel[PatientData]):
    pass
