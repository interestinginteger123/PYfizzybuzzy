from fizzbuzz import LambdaInteractor
from unittest.mock import Mock
import pytest
def test_lambda_for_five_modulus():
    #ARRANGE
    dictthing={'Fizz':3,'Buzz':5}
    result = 'Buzz'
    #ACT
    FIZZBUZZ = LambdaInteractor(dictthing)
    value = FIZZBUZZ.output(5)
    #ASSERT
    assert value == result

def test_lambda_for_three_modulus():
    #ARRANGE
    dictthing={'Fizz':3,'Buzz':5}
    result = 'Fizz'
    #ACT
    FIZZBUZZ = LambdaInteractor(dictthing)
    value = FIZZBUZZ.output(3)
    #ASSERT
    assert value == result

def test_lambda_for_both_modulus():
    #ARRANGE
    dictthing={'Fizz':3,'Buzz':5}
    result = 'FizzBuzz'
    #ACT
    FIZZBUZZ = LambdaInteractor(dictthing)
    value = FIZZBUZZ.output(15)
    #ASSERT
    assert value == result

def test_zero_result():
    #ARRANGE
    dictthing={'Fizz':3,'Buzz':5}
    result = ''
    #ACT
    FIZZBUZZ = LambdaInteractor(dictthing)
    value = FIZZBUZZ.output(1)
    #ASSERT
    assert value == result

def test_zero_error_bad_dict():
    with pytest.raises(Exception):
    #ARRANGE
        dictthing={'Fizz':3,'Buzz':'Error'}
    #ACT
        FIZZBUZZ = LambdaInteractor(dictthing)
        
    #ASSERT
        value = FIZZBUZZ.output(1)

def test_zero_error_bad_dict():
    with pytest.raises(Exception):
    #ARRANGE
        dictthing={'Fizz':3,'Buzz':'Error'}
    #ACT
        FIZZBUZZ = LambdaInteractor(dictthing)
        
    #ASSERT
        value = FIZZBUZZ.output(1)