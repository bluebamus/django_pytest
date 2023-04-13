class SomethingExport:
    val1 = 1000
    val2 = 1000
    val3 = 1000

    def val(self):
        return sum([self.val1, self.val2, self.val3])


def some_export_func():
    return {"message": "SUCCESS"}
