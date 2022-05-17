from server.instance import server
from controllers.senatran import *
from controllers.sus import *
import Configs
import Log

log = Log.get_logger(__name__)

if __name__ == "__main__":
    try:
        Configs.remove_dir(Configs.set_tmp_path("cnh",""))
        Configs.remove_dir(Configs.set_tmp_path("crlv",""))
        Configs.remove_dir(Configs.set_tmp_path("vacinas",""))
        server.run()
    except Exception as e:
        log.error(e)
        Log.send_alert_error(e)