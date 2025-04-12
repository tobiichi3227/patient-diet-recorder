import os
import unittest

import db
from constants import (
    ACCT_ALREADY_EXISTS,
    ACCT_CREATED,
    ACCT_DELETED,
    ACCT_NOT_EXIST,
    AUTH_FAIL_PASSWORD,
    AUTH_SUCCESS,
)
from db import AccountType

TEST_DB = "test_accounts.db"


class TestDBOperations(unittest.TestCase):
    def setUp(self):
        db.ACCOUNTS_DB = TEST_DB
        db.create_table()

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_add_account_success(self):
        result = db.add_account("user1", "pass1", AccountType.PATIENT)
        self.assertEqual(result, ACCT_CREATED)

    def test_add_account_duplicate(self):
        db.add_account("user1", "pass1", AccountType.PATIENT)
        result = db.add_account("user1", "pass1", AccountType.PATIENT)
        self.assertEqual(result, ACCT_ALREADY_EXISTS)

    def test_authenticate_success(self):
        db.add_account("user1", "pass1", AccountType.PATIENT)
        result = db.authenticate("user1", "pass1")
        self.assertEqual(result, AUTH_SUCCESS)

    def test_authenticate_wrong_password(self):
        db.add_account("user1", "pass1", AccountType.PATIENT)
        result = db.authenticate("user1", "wrongpass")
        self.assertEqual(result, AUTH_FAIL_PASSWORD)

    def test_authenticate_nonexistent(self):
        result = db.authenticate("ghost", "nopass")
        self.assertEqual(result, ACCT_NOT_EXIST)

    def test_delete_account(self):
        db.add_account("user1", "pass1", AccountType.PATIENT)
        result = db.delete_account("user1")
        self.assertEqual(result, ACCT_DELETED)

        result = db.authenticate("user1", "pass1")
        self.assertEqual(result, ACCT_NOT_EXIST)

    def test_get_account_type(self):
        db.add_account("user1", "pass1", AccountType.MONITOR)
        acct_type = db.get_account_type("user1")
        self.assertEqual(acct_type, AccountType.MONITOR)

    def test_get_password(self):
        db.add_account("user1", "pass1", AccountType.PATIENT)
        password = db.get_password("user1")
        self.assertEqual(password, "pass1")

    def test_get_all_accounts(self):
        db.add_account("user1", "pass1", AccountType.PATIENT)
        db.add_account("user2", "pass2", AccountType.MONITOR)
        accounts = db.get_all_accounts()
        self.assertEqual(len(accounts), 2)

    def test_get_patient_accounts(self):
        db.add_account("patient1", "patient1", AccountType.PATIENT)
        db.add_account("monitor1", "monitor1", AccountType.MONITOR)
        patients = db.get_patient_accounts()
        usernames = [acct[1] for acct in patients]
        self.assertIn("patient1", usernames)
        self.assertNotIn("monitor1", usernames)


if __name__ == "__main__":
    unittest.main()
