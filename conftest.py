import pytest, os
import pytest_html
from selenium import webdriver

# driver = webdriver.Chrome()
@pytest.fixture(scope="class", autouse=True)
def tc_setup(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Lauch Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Lauch Firefox")
    else:
        driver = webdriver.Edge()
        print("Lauch Edge")

    request.cls.driver = driver
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    yield driver

    print("Log off")
    print("Close browser")
    # driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://www.yatra.com")
    # all params:
    #   parser.addoption("--browser", action="store", default="chrome", help="The browser to use for testing.")
    
# for headless mode:
# options.add_argument("--headless")
# pytest test_name --headless    


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


# def capture_screenshot(filename):
#     driver.save_screenshot(filename)

# @pytest.mark.usefixtures("tc_setup")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    driver = webdriver.Chrome()
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            filename = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, filename)
            print(destination_file)
            driver.save_screenshot(destination_file)
            # capture_screenshot(destination_file)
            if filename:
                html = '<div><img src="%s" alt="screenshot" style="width:340px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' %filename
                extras.append(pytest_html.extras.html(html))
        report.extras = extras
        
def pytest_html_report_title(report):
    report.title = "Experiment test reports"