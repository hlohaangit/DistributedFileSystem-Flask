

# !/usr/bin/python
# coding=UTF-8


from . import options
from . import snowflake_m1


class DefaultIdGenerator:

    def __init__(self):
        self.snowflake = None

    def set_id_generator(self, option: options.IdGeneratorOptions):


        if option.base_time < 100000:
            raise ValueError("base time error.")

        self.snowflake = snowflake_m1.SnowFlakeM1(option)

    def next_id(self) -> int:


        if self.snowflake is None:
            raise ValueError("please set id generator at first.")
        return self.snowflake.next_id()
