from ..handler import JsonHandler

class LottieManager:
    WAKEUP_LOTTIE = JsonHandler.load_json(json_file_path="./data/wakeup_lottie.json")
    LOGIN_SUCCESS_LOTTIE = JsonHandler.load_json(json_file_path="./data/login_success_lottie.json")