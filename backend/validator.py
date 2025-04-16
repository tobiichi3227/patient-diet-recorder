import re
from datetime import date, datetime
from datetime import time as time_cls
from typing import Any

from pydantic import (
    BaseModel,
    Field,
    RootModel,
    model_validator,
    validator,
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
    food: int
    water: int
    urination: int
    defecation: int



class DailyRecord(BaseModel):
    data: list[RecordItem]
    count: int
    recordDate: str
    foodSum: int
    waterSum: int
    urinationSum: int
    defecationSum: int
    weight: str

    @model_validator(mode="after")
    def validate_all(self):
        assert self.count == len(self.data), "count does not match data length"

        for field in ["food", "water", "urination", "defecation"]:
            expected = sum(getattr(item, field) for item in self.data)
            actual = getattr(self, f"{field}Sum")
            assert actual == expected, (
                f"{field}Sum expected {expected}, got {actual}"
            )
            assert isinstance(actual, int)

        record_date = parse_record_date(self.recordDate)
        assert record_date <= date.today(), (
            f"recordDate is in the future: {self.recordDate}"
        )

        if self.weight != "NaN":
            assert re.fullmatch(r"\d+ kg", self.weight), (
                f"invalid weight format: {self.weight}"
            )
            weight_val = int(self.weight.split()[0])
            assert weight_val > 0, "weight must be a positive integer"
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
    def split_records(cls, values: Any):
        reserved = {
            "isEditing",
            "limitAmount",
            "foodCheckboxChecked",
            "waterCheckboxChecked",
        }
        records = {k: v for k, v in values.items() if k not in reserved}

        for key in records:
            assert parse_date_key(key) <= date.today(), (
                f"record key {key} is in the future"
            )

        return values


class UpdateDataModel(RootModel[PatientData]):
    pass
