import django
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import BaseValidator

import jsonschema

SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "amount": {"type": "number"}
    },
    "required": ["id", "amount"]
}


class JSONSchemaValidator(BaseValidator):
    def compare(self, input_value, schema):
        try:
            for object_ in input_value:
                jsonschema.validate(object_, schema)

        except jsonschema.exceptions.ValidationError:
            raise django.core.exceptions.ValidationError(
                'Validate error. '
                'Template: [{"id": 1, "amount": 2}, {"id": 2, "amount": 3}, ...]')
