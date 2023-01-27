import user_interface as ui
import logger as lg
import crude as c


lg.logging.info('Start')
c.init_data_base('base_phone.csv')
ui.ls_menu()