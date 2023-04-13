from mocking_export import SomethingExport, some_export_func


class SomethingImport2:
    val1 = 100
    val2 = 200
    val3 = 300

    def val(self):
        return sum([self.val1, self.val2, self.val3, SomethingExport().val()])

    def func(self):
        return some_export_func()
