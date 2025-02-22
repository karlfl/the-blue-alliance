from flask import abort, Blueprint
from google.appengine.api import users as gae_login

from backend.common.environment import Environment
from backend.web.handlers.admin.api_auth import (
    api_auth_add,
    api_auth_delete,
    api_auth_delete_post,
    api_auth_edit,
    api_auth_edit_post,
    api_auth_manage,
)
from backend.web.handlers.admin.authkeys import authkeys_get, authkeys_post
from backend.web.handlers.admin.event import (
    event_create,
    event_delete,
    event_delete_matches,
    event_detail,
    event_detail_post,
    event_edit,
    event_edit_post,
    event_list,
    event_remap_teams_post,
)
from backend.web.handlers.admin.landing import (
    landing_edit,
)
from backend.web.handlers.admin.match import (
    match_add,
    match_dashboard,
    match_delete,
    match_delete_post,
    match_detail,
    match_edit,
    match_edit_post,
)
from backend.web.handlers.admin.sitevars import (
    sitevar_create,
    sitevar_edit,
    sitevar_edit_post,
    sitevars_list,
)
from backend.web.handlers.admin.team import (
    team_detail,
    team_list,
    team_robot_name_update,
    team_website_update,
)
from backend.web.handlers.admin.team_media_mod import (
    team_media_mod_add,
    team_media_mod_add_post,
    team_media_mod_edit,
    team_media_mod_edit_post,
    team_media_mod_list,
)
from backend.web.profiled_render import render_template


"""
This is a special interface available to TBA admins to manage data
"""

admin_routes = Blueprint("admin", __name__, url_prefix="/admin")


@admin_routes.before_request
def require_gae_admin() -> None:
    """
    Ensure that only admins can access this blueprint
    """
    if not gae_login.is_current_user_admin():
        abort(401)


@admin_routes.route("/")
def admin_home() -> str:
    template_values = {
        "memcache_stats": {
            "hits": 0,
            "misses": 0,
        },
        "databasequery_stats": {
            "hits": 0,
            "misses": 0,
        },
        "users": [],
        "suggestions_count": 0,
        "contbuild_enabled": False,
        "git_branch_name": "",
        "build_time": "",
        "build_number": "",
        "commit_hash": "",
        "commit_author": "",
        "commit_date": "",
        "commit_msg": "",
        "debug": Environment.is_dev(),
    }
    return render_template("admin/index.html", template_values)


@admin_routes.route("/tasks")
def task_launcher() -> str:
    return render_template("admin/tasks.html")


# More complex endpoints should be split out into their own files
admin_routes.add_url_rule("/api_auth/add", view_func=api_auth_add, methods=["GET"])
admin_routes.add_url_rule(
    "/api_auth/delete/<auth_id>", view_func=api_auth_delete, methods=["GET"]
)
admin_routes.add_url_rule(
    "/api_auth/delete/<auth_id>", view_func=api_auth_delete_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/api_auth/edit/<auth_id>", view_func=api_auth_edit, methods=["GET"]
)
admin_routes.add_url_rule(
    "/api_auth/edit/<auth_id>", view_func=api_auth_edit_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/api_auth/manage", view_func=api_auth_manage, methods=["GET"]
)
admin_routes.add_url_rule("/authkeys", view_func=authkeys_get, methods=["GET"])
admin_routes.add_url_rule("/authkeys", view_func=authkeys_post, methods=["POST"])
admin_routes.add_url_rule("/event/create", view_func=event_create, methods=["GET"])
admin_routes.add_url_rule(
    "/event/<event_key>/delete", view_func=event_delete, methods=["GET", "POST"]
)
admin_routes.add_url_rule(
    "/event/<event_key>/edit", view_func=event_edit, methods=["GET"]
)
admin_routes.add_url_rule(
    "/event/<event_key>/edit", view_func=event_edit_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/event/edit",
    view_func=event_edit_post,
    defaults={"event_key": None},
    methods=["POST"],
)
admin_routes.add_url_rule("/event/<event_key>", view_func=event_detail, methods=["GET"])
admin_routes.add_url_rule(
    "/event/<event_key>", view_func=event_detail_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/event/remap_teams/<event_key>", view_func=event_remap_teams_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/event/delete_matches/<event_key>/<comp_level>/<to_delete>",
    view_func=event_delete_matches,
    methods=["GET"],
)
admin_routes.add_url_rule("/events", view_func=event_list, defaults={"year": None})
admin_routes.add_url_rule("/events/<int:year>", view_func=event_list)
admin_routes.add_url_rule("/matches", view_func=match_dashboard, methods=["GET"])
admin_routes.add_url_rule("/match/add", view_func=match_add, methods=["POST"])
admin_routes.add_url_rule("/match/<match_key>", view_func=match_detail, methods=["GET"])
admin_routes.add_url_rule(
    "/match/edit/<match_key>", view_func=match_edit, methods=["GET"]
)
admin_routes.add_url_rule(
    "/match/edit/<match_key>", view_func=match_edit_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/match/delete/<match_key>", view_func=match_delete, methods=["GET"]
)
admin_routes.add_url_rule(
    "/match/delete/<match_key>", view_func=match_delete_post, methods=["POST"]
)
admin_routes.add_url_rule("/sitevars", view_func=sitevars_list)
admin_routes.add_url_rule("/sitevar/create", view_func=sitevar_create, methods=["GET"])
admin_routes.add_url_rule(
    "/sitevar/edit/<sitevar_key>", view_func=sitevar_edit, methods=["GET"]
)
admin_routes.add_url_rule(
    "/sitevar/edit/<sitevar_key>", view_func=sitevar_edit_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/main_landing", view_func=landing_edit, methods=["GET", "POST"]
)
admin_routes.add_url_rule("/teams", view_func=team_list)
admin_routes.add_url_rule("/teams/<int:page_num>", view_func=team_list)
admin_routes.add_url_rule("/team/<int:team_number>", view_func=team_detail)
admin_routes.add_url_rule(
    "/team/website", view_func=team_website_update, methods=["POST"]
)
admin_routes.add_url_rule("/media/modcodes/list", view_func=team_media_mod_list)
admin_routes.add_url_rule(
    "/media/modcodes/list/<int:year>", view_func=team_media_mod_list
)
admin_routes.add_url_rule(
    "/media/modcodes/list/<int:year>/<int:page_num>", view_func=team_media_mod_list
)
admin_routes.add_url_rule("/media/modcodes/add", view_func=team_media_mod_add)
admin_routes.add_url_rule(
    "/media/modcodes/add", view_func=team_media_mod_add_post, methods=["POST"]
)
admin_routes.add_url_rule(
    "/media/modcodes/edit/<int:team_number>/<int:year>",
    view_func=team_media_mod_edit,
)
admin_routes.add_url_rule(
    "/media/modcodes/edit/<int:team_number>/<int:year>",
    view_func=team_media_mod_edit_post,
    methods=["POST"],
)
admin_routes.add_url_rule(
    "/team/set_robot_name", view_func=team_robot_name_update, methods=["POST"]
)
