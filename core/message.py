class FontColors:
    RED: str = '\033[31m'
    GREEN: str = '\033[32m'
    YELLOW: str = '\033[33m'
    RESET: str = '\033[0m'


def LOAD_FILE_MSG(file_name: str) -> str:
    result: str = f'Loaded {FontColors.YELLOW}{file_name}{FontColors.RESET}'
    return result


def ACCURACY_MSG(accuracy: float) -> str:
    result: str = f'Accuracy {FontColors.YELLOW}{accuracy * 100:.3g}{FontColors.RESET}'
    return result


def MEASURE_ACCURACY_MSG(n_samples: int) -> str:
    result: str = f'Measure accuracy with {n_samples} samples...'
    return result


def N_SAMPLES_INPUT_GUIDE(max_samples: int) -> str:
    result: str = f'How many samples? {FontColors.GREEN}(1-{max_samples}){FontColors.RESET} : '
    return result
