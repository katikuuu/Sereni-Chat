from .base_s_state import BaseSState


class WakeupLottieSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return "wakeup_lottie"
    
    @staticmethod
    def get_default() -> bool:
        return False