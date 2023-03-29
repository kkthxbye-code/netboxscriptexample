from extras.scripts import ObjectVar
from dcim.models import Device

class BaseScript:
    base_script_device = ObjectVar(
        model=Device,
        required=False
    )
