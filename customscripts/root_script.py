from dcim.models import Device
from extras.scripts import ObjectVar
from scripts.util.common import shared_function
from netbox_script_manager.scripts import CustomScript


class RootScript1(CustomScript):
    class Meta:
        name = "Root Script 1"
        description = "Testing"

    device = ObjectVar(
        model=Device,
        required=False
    )

    def run(self, data, commit):
        self.log_success("RootScript1")
        self.log_success(shared_function())

class RootScript2(CustomScript):
    class Meta:
        name = "Root Script 2"
        description = "Testing"

    device = ObjectVar(
        model=Device,
        required=False
    )

    def run(self, data, commit):
        self.log_success("RootScript2")
        self.log_success(shared_function())