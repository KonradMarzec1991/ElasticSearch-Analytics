from enum import Enum


class Error(Enum):
    AGE_ERROR = 'Age must greater than 0'
    MARTIAL_ERROR = 'Unmarried or Married allowed'
    GENDER_ERROR = 'Gender must be female or male'