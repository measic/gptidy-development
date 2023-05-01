from enum import Enum

class Operation(Enum):
    RenameVariable = 1
    ExtractFunction = "extract this code as function "
    ExtractDuplicateCode = "find duplicate code and extract to a function"

samples = {
    Operation.RenameVariable: {
        "prompt": lambda variables: "Give meaningful variable names ONLY to: " + variables + ". Use provided context.",
    },
}