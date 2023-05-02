from enum import Enum

class Operation(Enum):
    RenameVariable = 1
    ExtractFunction = "extract this code as function "
    ExtractDuplicateCode = "find duplicate code and extract to a function"

prompts = {
    Operation.RenameVariable: {
        "prompt": lambda variables: "Rename instances of variables [" + variables + "] to have meaningful names. Ignore any variables in code not mentioned here.",
    },
    Operation.ExtractFunction: {
        "prompt": lambda variables: "Extract this code as function " + variables + ". Do not change anything else in code",
    },
}