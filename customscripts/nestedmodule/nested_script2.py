from dcim.models import Device
from extras.scripts import ObjectVar
from ..util.common import shared_function
from netbox_script_manager.scripts import CustomScript

class NestedScript2(CustomScript):
    class Meta:
        name = "Nested Script 2"
        description = "Testing"

    device = ObjectVar(
        model=Device,
        required=False
    )

    def run(self, data, commit):
        self.log_success("NestedScript2")
        self.log_success(shared_function())