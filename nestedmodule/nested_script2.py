from dcim.models import Device
from extras.scripts import Script, ObjectVar
from scripts.util.common import shared_function

class NestedScript2(Script):
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