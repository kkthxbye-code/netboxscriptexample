from dcim.models import Device
from extras.scripts import ObjectVar
from .base_script import BaseScript
from ..util.common import shared_function
from netbox_script_manager.scripts import CustomScript

class NestedScript1(CustomScript, BaseScript):
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