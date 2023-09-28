# Description: This file contains all the reply and inline keyboard markups used in the bot.
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from AdminBot.content import KEY_MARKUP
from AdminBot.content import MESSAGES
from config import CLIENT_TOKEN, HIDY_BOT_ID
from Utils.utils import all_configs_settings, rial_to_toman


# Main Menu Reply Keyboard Markup
def main_menu_keyboard_markup():
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    #markup.add(KeyboardButton(KEY_MARKUP['USERS_LIST']))
    #markup.add(KeyboardButton(KEY_MARKUP['USERS_SEARCH']), KeyboardButton(KEY_MARKUP['ADD_USER']))
    markup.add(KeyboardButton(KEY_MARKUP['SERVERS_MANAGEMENT']))
    markup.add(KeyboardButton(KEY_MARKUP['USERS_SEARCH']))
    if CLIENT_TOKEN:
        markup.add(KeyboardButton(KEY_MARKUP['USERS_BOT_MANAGEMENT']))
    markup.add()
    markup.add(KeyboardButton(KEY_MARKUP['SERVER_STATUS']), KeyboardButton(KEY_MARKUP['ABOUT_BOT']),
               KeyboardButton(KEY_MARKUP['SERVER_BACKUP']))

    return markup


# Users List Inline Keyboard Markup
def users_list_markup(server_id, users, page=1):
    markup = InlineKeyboardMarkup(row_width=3)
    USER_PER_PAGE = 20
    start = (page - 1) * USER_PER_PAGE
    end = start + USER_PER_PAGE
    keys = []

    for user in users[start:end]:
        status_tag = ""
        if user['last_connection'] == "Online" or user['last_connection'] == "آنلاین":
            status_tag = "🔵"
        else:
            status_tag = "🟡"
        if user['remaining_day'] == 0:
            status_tag = "🔴"
        if user['usage']['remaining_usage_GB'] <= 0:
            status_tag = "🔴️"

        keys.append(InlineKeyboardButton(f"{status_tag}|{user['name']}", callback_data=f"info:{user['uuid']}"))
    markup.add(*keys)
    if page < len(users) / USER_PER_PAGE:
        markup.add(InlineKeyboardButton(KEY_MARKUP['NEXT_PAGE'], callback_data=f"next:{page + 1}"), row_width=2)
    if page > 1:
        markup.add(InlineKeyboardButton(KEY_MARKUP['PREV_PAGE'], callback_data=f"next:{page - 1}"), row_width=1)
    if server_id != "None":
        markup.add(InlineKeyboardButton(KEY_MARKUP['ADD_USER'], callback_data=f"server_add_user:{server_id}"))
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_SEARCH'], callback_data=f"server_search_user:{server_id}"))
        markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_server_selected:{server_id}"))
    return markup


# Single User Inline Keyboard Markup
def user_info_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_USER'], callback_data=f"user_config:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_USER'], callback_data=f"user_edit:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['DELETE_USER'], callback_data=f"user_delete:{uuid}"))
    return markup


# Single User Edit Inline Keyboard Markup
def edit_user_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_NAME'], callback_data=f"user_edit_name:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_USAGE'], callback_data=f"user_edit_usage:{uuid}"),
               InlineKeyboardButton(KEY_MARKUP['RESET_USAGE'], callback_data=f"user_edit_reset_usage:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_DAYS'], callback_data=f"user_edit_days:{uuid}"),
               InlineKeyboardButton(KEY_MARKUP['RESET_DAYS'], callback_data=f"user_edit_reset_days:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_COMMENT'], callback_data=f"user_edit_comment:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['UPDATE_MESSAGE'], callback_data=f"user_edit_update:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_user_panel:{uuid}"))
    return markup


# Add User Reply Keyboard Markup
def while_add_user_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['CANCEL']))
    return markup


# Edit User Reply Keyboard Markup
def while_edit_user_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['CANCEL']))
    return markup


# Confirm Add User Reply Keyboard Markup
def confirm_add_user_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['CONFIRM']))
    markup.add(KeyboardButton(KEY_MARKUP['CANCEL']))
    return markup


# Subscription URL Inline Keyboard Markup
def sub_url_user_list_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_DIR'], callback_data=f"conf_dir:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_SUB_AUTO'], callback_data=f"conf_sub_auto:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_SUB'], callback_data=f"conf_sub_url:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_SUB_B64'], callback_data=f"conf_sub_url_b64:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_CLASH'], callback_data=f"conf_clash:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_HIDDIFY'], callback_data=f"conf_hiddify:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_SING_BOX'], callback_data=f"conf_sub_sing_box:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_FULL_SING_BOX'],
                                        callback_data=f"conf_sub_full_sing_box:{uuid}"))

    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_user_panel:{uuid}"))

    return markup


# Subscription Configs Inline Keyboard Markup
def sub_user_list_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Vless', callback_data=f"conf_dir_vless:{uuid}"))
    markup.add(InlineKeyboardButton('Vmess', callback_data=f"conf_dir_vmess:{uuid}"))
    markup.add(InlineKeyboardButton('Trojan', callback_data=f"conf_dir_trojan:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_sub_url_user_list:{uuid}"))
    return markup


# Search User Inline Keyboard Markup
def search_user_markup(server_id=None):
    callback_data = server_id if server_id else "None"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_USER_NAME'], callback_data=f"search_name:{callback_data}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_USER_UUID'], callback_data=f"search_uuid:{callback_data}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_USER_CONFIG'], callback_data=f"search_config:{callback_data}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_EXPIRED_USERS'], callback_data=f"search_expired:{callback_data}"))
    if server_id:
        markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_server_user_list:{server_id}"))
    return markup


# Users Bot Management - Inline Keyboard Markup
def users_bot_management_markup(value=None):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton(KEY_MARKUP['USERS_BOT_ORDERS_STATUS'], callback_data=f"users_bot_orders_status:None"),
        InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SUB_STATUS'], callback_data=f"users_bot_sub_status:None"))
    # markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_ADD_PLAN'], callback_data=f"users_bot_add_plan:None"),
    #            InlineKeyboardButton(KEY_MARKUP['USERS_BOT_DEL_PLAN'], callback_data=f"users_bot_list_plans:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SEND_MESSAGE_TO_USERS'],
                                    callback_data=f"users_bot_send_msg_users:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO'], callback_data=f"users_bot_owner_info:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS'], callback_data=f"users_bot_settings:None"))
    return markup


# Users Bot Management - Settings - Inline Keyboard Markup
def users_bot_management_settings_markup(settings):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    status_hyperlink = "✅" if settings['visible_hiddify_hyperlink'] else "❌"
    status_three_rand = "✅" if settings['three_random_num_price'] else "❌"
    status_panel_auto_backup = "✅" if settings['panel_auto_backup'] else "❌"
    status_bot_auto_backup = "✅" if settings['bot_auto_backup'] else "❌"
    status_force_join = "✅" if settings['force_join_channel'] else "❌"
    status_buy_sub = "✅" if settings['buy_subscription_status'] else "❌"
    status_renewal_sub = "✅" if settings['renewal_subscription_status'] else "❌"

    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_SHOW_HIDI_LINK']} | {status_hyperlink}",
                                    callback_data=f"users_bot_settings_hyperlink:{settings['visible_hiddify_hyperlink']}"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_SHOW_THREE_RAND']} | {status_three_rand}",
                                    callback_data=f"users_bot_settings_three_rand_price:{settings['three_random_num_price']}"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_AUTO_BACKUP']} | {status_panel_auto_backup}",
                             callback_data=f"users_bot_settings_panel_auto_backup:{settings['panel_auto_backup']}"),
               InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_BOT_AUTO_BACKUP']} | {status_bot_auto_backup}",
                                    callback_data=f"users_bot_settings_bot_auto_backup:{settings['bot_auto_backup']}")
               )
    
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_BUY_SUBSCRIPTION_STATUS']} | {status_buy_sub}",
                                    callback_data=f"users_bot_settings_buy_sub_status:{settings['buy_subscription_status']}"),
               InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_SUBSCRIPTION_STATUS']} | {status_renewal_sub}",
                                    callback_data= f"users_bot_settings_renewal_sub_status:{settings['renewal_subscription_status']}"))
    
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_CHANNEL_ّFORCE_JOIN']} | {status_force_join}",
                                    callback_data=f"users_bot_settings_force_join:{settings['force_join_channel']}"),
               InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_CHANNEL_ID'],
                                    callback_data=f"users_bot_settings_channel_id:{settings['channel_id']}"))

    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_SET_WELCOME_MSG'],
                                    callback_data=f"users_bot_settings_set_welcome_msg:None"),
               InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_MANUAL'],
                                    callback_data="users_bot_settings_panel_manual_menu:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_VISIBLE_SUBS'],
                                    callback_data=f"users_bot_settings_visible_sub_menu:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_TEST_SUB'],
                                    callback_data=f"users_bot_settings_test_sub_menu:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_NOTIF_REMINDER'],
                                    callback_data=f"users_bot_settings_notif_reminder_menu:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_MIN_DEPO'],
                                    callback_data=f"users_bot_settings_min_depo:{settings['min_deposit_amount']}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_METHOD'],
                                    callback_data=f"users_bot_settings_renewal_method_menu:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_BACKUP_BOT'],
                                    callback_data=f"users_bot_settings_backup_bot:None"),
               InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_RESTORE_BOT'],
                                    callback_data=f"users_bot_settings_restore_bot:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"users_bot_management_menu:None"))
    return markup

def users_bot_management_settings_renewal_method_markup(settings):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    default, advanced, fairly = "❌", "❌", "❌"
    
    if settings['renewal_method'] == 1:
        default = "✅"
    elif settings['renewal_method'] == 2:
        advanced = "✅"
    elif settings['renewal_method'] == 3:
        fairly = "✅"
        
        
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_METHOD_DEFAULT']} | {default}",
                                    callback_data=f"users_bot_settings_renewal_method:1"),
                InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_METHOD_ADVANCED']} | {advanced}",
                                    callback_data=f"users_bot_settings_renewal_method:2"),
                InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_METHOD_FAIRLY']} | {fairly}",
                      callback_data=f"users_bot_settings_renewal_method:3"),
    )
               
    if settings['renewal_method'] == 2:
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_METHOD_ADVANCED_DAYS'],
                                        callback_data=f"users_bot_settings_renewal_method_advanced_days:None"))
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_RENEWAL_METHOD_ADVANCED_USAGE'],
                                        callback_data=f"users_bot_settings_renewal_method_advanced_usage:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"users_bot_settings:None"))
    return markup

def users_bot_management_settings_test_sub_markup(settings):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    status_test_sub = "✅" if settings['test_subscription'] else "❌"
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_TEST_SUB']} | {status_test_sub}",
                                    callback_data=f"users_bot_settings_test_sub:test_subscription"))
    if settings['test_subscription']:
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_TEST_SUB_SIZE'],
                                        callback_data=f"users_bot_settings_test_sub_size:None"))
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_TEST_SUB_DAYS'],
                                        callback_data=f"users_bot_settings_test_sub_days:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"users_bot_settings:None"))
    return markup


def users_bot_management_settings_notif_reminder_markup(settings):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    status_test_sub = "✅" if settings['reminder_notification'] else "❌"
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_NOTIF_REMINDER']} | {status_test_sub}",
                                    callback_data=f"users_bot_settings_notif_reminder:reminder_notification"))
    if settings['reminder_notification']:
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_NOTIF_REMINDER_USAGE'],
                                        callback_data=f"users_bot_settings_notif_reminder_usage:None"))
        markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_NOTIF_REMINDER_DAYS'],
                                        callback_data=f"users_bot_settings_notif_reminder_days:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"users_bot_settings:None"))
    return markup


def users_bot_management_settings_visible_sub_markup(settings):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    status_visible_conf_dir = "✅" if settings['visible_conf_dir'] else "❌"
    status_conf_sub_auto = "✅" if settings['visible_conf_sub_auto'] else "❌"
    status_conf_sub_url = "✅" if settings['visible_conf_sub_url'] else "❌"
    status_conf_sub_url_b64 = "✅" if settings['visible_conf_sub_url_b64'] else "❌"
    status_conf_clash = "✅" if settings['visible_conf_clash'] else "❌"
    status_conf_hiddify = "✅" if settings['visible_conf_hiddify'] else "❌"
    status_conf_sub_sing_box = "✅" if settings['visible_conf_sub_sing_box'] else "❌"
    status_conf_sub_full_sing_box = "✅" if settings['visible_conf_sub_full_sing_box'] else "❌"

    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_DIR']} | {status_visible_conf_dir}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_dir"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_SUB_AUTO']} | {status_conf_sub_auto}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_sub_auto"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_SUB']} | {status_conf_sub_url}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_sub_url"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_SUB_B64']} | {status_conf_sub_url_b64}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_sub_url_b64"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_CLASH']} | {status_conf_clash}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_clash"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_HIDDIFY']} | {status_conf_hiddify}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_hiddify"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_SING_BOX']} | {status_conf_sub_sing_box}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_sub_sing_box"))
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['CONFIGS_FULL_SING_BOX']} | {status_conf_sub_full_sing_box}",
                                    callback_data=f"users_bot_settings_visible_sub:visible_conf_sub_full_sing_box"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"users_bot_settings:None"))
    return markup


def users_bot_management_settings_panel_manual_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_MANUAL_ANDROID'],
                                    callback_data=f"users_bot_settings_panel_manual:msg_manual_android"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_MANUAL_IOS'],
                                    callback_data=f"users_bot_settings_panel_manual:msg_manual_ios"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_MANUAL_WIN'],
                                    callback_data=f"users_bot_settings_panel_manual:msg_manual_windows"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_MANUAL_MAC'],
                                    callback_data=f"users_bot_settings_panel_manual:msg_manual_mac"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS_PANEL_MANUAL_LIN'],
                                    callback_data=f"users_bot_settings_panel_manual:msg_manual_linux"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"users_bot_settings:None"))
    return markup


# Users Bot Management - Edit Owner Info - Inline Keyboard Markup
def users_bot_edit_owner_info_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO_EDIT_USERNAME'],
                                    callback_data=f"users_bot_owner_info_edit_username:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO_EDIT_CARD_NUMBER'],
                                    callback_data=f"users_bot_owner_info_edit_card_number:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO_EDIT_CARD_NAME'],
                                    callback_data=f"users_bot_owner_info_edit_card_name:None"))
    return markup


# Server Management - Server List - Inline Keyboard Markup
def servers_management_markup(servers):
    markup = InlineKeyboardMarkup(row_width=1)
    keys = []
    if servers:
        for server in servers:
            if server['status']:
                keys.append(InlineKeyboardButton(
                    f"{server['title']}",
                    callback_data=f"server_selected:{server['id']}"))
    keys.append(InlineKeyboardButton(
                KEY_MARKUP['ADD_SERVER'],
                callback_data=f"add_server:None"))
    markup.add(*keys)
    return markup

# Server Management - Server List - Inline Keyboard Markup
def server_selected_markup(server_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['SERVER_LIST_OF_USERS'],
                                    callback_data=f"server_list_of_users:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SERVER_LIST_OF_PLANS'],
                                    callback_data=f"server_list_of_plans:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_SERVER'],
                                    callback_data=f"edit_server:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_server_management:None"))
    
    return markup

# Server Management - Server Delete - Inline Keyboard Markup
def server_delete_markup(server_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIRM'],
                                    callback_data=f"confirm_delete_server:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CANCEL'],
                                    callback_data=f"server_selected:{server_id}"))
    return markup


# Server Management - Server Edit - Inline Keyboard Markup
def server_edit_markup(server_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['SERVER_EDIT_TITLE'],
                                    callback_data=f"server_edit_title:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SERVER_EDIT_USER_LIMIT'],
                                    callback_data=f"server_edit_user_limit:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SERVER_EDIT_URL'],
                                    callback_data=f"server_edit_url:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['DELETE_SERVER'],
                                    callback_data=f"delete_server:{server_id}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_server_selected:{server_id}"))

    return markup
# Users Bot Management - Plans List - Inline Keyboard Markup
def plans_list_markup(plans, server_id, delete_mode=False):
    markup = InlineKeyboardMarkup(row_width=1)
    plan_selected_callback_data = "users_bot_del_plan:" if delete_mode else "info_plan_selected:" 
    back_callback_data = "back_to_server_list_of_plans:" if delete_mode else "back_to_server_selected:"
    keys = []
    if plans:
        for plan in plans:
            keys.append(InlineKeyboardButton(
                f"{plan['size_gb']}{MESSAGES['GB']} | {plan['days']}{MESSAGES['DAY']} | {rial_to_toman(plan['price'])} {MESSAGES['TOMAN']}",
                callback_data = f"{plan_selected_callback_data}{plan['id']}"))
    if not delete_mode:
        keys.append(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_ADD_PLAN'], callback_data=f"users_bot_add_plan:{server_id}"))
        keys.append(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_DEL_PLAN'], callback_data=f"users_bot_list_plans:{server_id}"))
    keys.append(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"{back_callback_data}{server_id}"))
    markup.add(*keys)
    return markup

def plan_info_selected_markup(server_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_server_list_of_plans:{server_id}"))
    return markup


def start_bot_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    bot_id = HIDY_BOT_ID.replace("@", "")
    markup.add(InlineKeyboardButton(KEY_MARKUP['SUPPORT_GROUP'], url=f"https://t.me/{bot_id}"))
    return markup
