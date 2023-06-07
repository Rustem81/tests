from hello import toyou, add, subtract


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
# def test_hello_add():
#    assert add(test_hello_add.x) == 12


def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9


def test_hello_add():
    assert add(test_hello_add.x) == 11


def test_hello_toyou():
    assert toyou("Student2") == "hi Student2"
    
    
# var=


def toyou(x):
    return f"hi {x}"


def add(x):
    return x + 1


def subtract(x):
    return x - 1

def main():
    opt = parse_opt(options)

    cfg = get_cfg(opt["config_path"])
    setup_logging(cfg["LOG_FILE"], cfg["LOG_LEVEL"])

    if not is_valid_cfg_options(cfg):
        logging.error("Invalid config: {}".format(cfg))
        return
    log_des = get_last_log(cfg["LOG_DIR"])

    report_path = os.path.join(cfg["REPORT_DIR"],
                               "report-{}.html".format(log_des.date))
    log_path = os.path.join(cfg["LOG_DIR"], log_des.name)

    is_need_process = (os.path.isfile(log_path) and
                       not os.path.isfile(report_path))
    if not is_need_process:
        logging.info("No log-files to process")
        return
    report, error_limit = log_process(log_path, cfg["REPORT_SIZE"])
    if error_limit > cfg["ERROR_LIMIT"]:
        logging.error("Errors: {}%".format(error_limit))
        return
    else:
        save_as_json(report_path, report)


