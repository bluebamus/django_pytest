from mocking_const import CONST


class SomethingImport:
    val1 = 100
    val2 = 200
    val3 = 300

    def val(self):
        return sum([self.val1, self.val2, self.val3, CONST])


def some_import_func():
    return {"message": "SUCCESS"}
