from dcim.models import Device
from extras.scripts import Script, ObjectVar
from .base_script import BaseScript
from scripts.util.common import shared_function

class NestedScript1(Script, BaseScript):
    class Meta:
        name = "Nested Script 1"
        description = "Testing"

    device = ObjectVar(
        model=Device,
        required=False
    )

    def run(self, data, commit):
        self.log_success("NestedScript1")
        self.log_success(shared_function())