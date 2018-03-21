# TODO validate type is in valid set of values for all below

fv_schema = {
    "type": "object",
    "properties": {
        "rate": {
            "type": "number"
        },
        "nper": {
            "type": "number"
        },
        "pmt": {
            "type": "number"
        },
        "pv": {
            "type": "number"
        },
        "type": {
            "type": "number"
        }
    },
    "required": ["rate", "nper", "pmt", "pv"]
}

pv_schema = {
    "type": "object",
    "properties": {
        "rate": {
            "type": "number"
        },
        "nper": {
            "type": "number"
        },
        "pmt": {
            "type": "number"
        },
        "fv": {
            "type": "number"
        },
        "type": {
            "type": "number"
        }
    },
    "required": ["rate", "nper", "pmt", "fv"]
}

npv_schema = {
    "type": "object",
    "properties": {
        "rate": {
            "type": "number"
        },
        "values": {
            "type": "array",
            "items": {
                "type": "number",
                "minItems": 1
            }
        }
    },
    "required": ["rate", "values"]
}

pmt_schema = {
    "type": "object",
    "properties": {
        "rate": {
            "type": "number"
        },
        "nper": {
            "type": "number"
        },
        "pv": {
            "type": "number"
        },
        "fv": {
            "type": "number"
        },
        "type": {
            "type": "number"
        }
    },
    "required": ["rate", "nper", "pv"]
}

ppmt_schema = {
    "type": "object",
    "properties": {
        "rate": {
            "type": "number"
        },
        "per": {
            "type": "number"
        },
        "nper": {
            "type": "number"
        },
        "pv": {
            "type": "number"
        },
        "fv": {
            "type": "number"
        },
        "type": {
            "type": "number"
        }
    },
    "required": ["rate", "per", "nper", "pv"]
}

irr_schema = {
    "type": "object",
    "properties": {
        "values": {
            "type": "array",
            "items": {
                "type": "number",
                "minItems": 1
            }
        }
    },
    "required": ["values"]
}

mirr_schema = {
    "type": "object",
    "properties": {
        "values": {
            "type": "array",
            "items": {
                "type": "number",
                "minItems": 1
            }
        },
        "finance_rate": {
            "type": "number"
        },
        "reinvest_rate": {
            "type": "number"
        }
    },
    "required": ["values", "finance_rate", "reinvest_rate"]
}

nper_schema = {
    "type": "object",
    "properties": {
        "rate": {
            "type": "number"
        },
        "pmt": {
            "type": "number"
        },
        "pv": {
            "type": "number"
        },
        "fv": {
            "type": "number"
        },
        "type": {
            "type": "number"
        }
    },
    "required": ["rate", "pmt", "pv"]
}

rate_schema = {
    "type": "object",
    "properties": {
        "nper": {
            "type": "number"
        },
        "pmt": {
            "type": "number"
        },
        "pv": {
            "type": "number"
        },
        "fv": {
            "type": "number"
        },
        "type": {
            "type": "number"
        },
        "guess": {
            "type": "number"
        }
    },
    "required": ["nper", "pmt", "pv", "fv"]
}
