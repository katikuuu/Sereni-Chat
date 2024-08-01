from .base_s_state import BaseSState


class FinishedLoginLottieSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return "finished_login_lottie"
    
    @staticmethod
    def get_default() -> bool:
        return False