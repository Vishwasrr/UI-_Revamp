import pytest

@pytest.mark.usefixtures("tc_setup")
class WebUtils:
    
    def capture_screenshot(self, filename):
        self.driver.save_screenshot(filename)