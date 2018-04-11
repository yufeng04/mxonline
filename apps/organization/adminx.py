import xadmin
from .models import CourseOrg, CityDict, Teacher


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'fav_nums', 'image', 'click_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'fav_nums', 'image', 'click_nums', 'address', 'city', 'add_time']
    list_filter = ['name', 'desc', 'fav_nums', 'image', 'click_nums', 'address', 'city']


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class CityDictAdmin(object):
    list_display = ['name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']


xadmin.site.register(CityDict, CityDictAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'image', 'click_nums', 'add_time']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'image', 'click_nums']


xadmin.site.register(Teacher, TeacherAdmin)