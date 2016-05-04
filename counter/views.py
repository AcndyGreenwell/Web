from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
import subprocess
from django.core.urlresolvers import reverse
from .models import *
from .forms import ZoneForm, TimeTableForm, ZoneOptionForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import Http404


sql = 'SELECT counter_camera.id, counter_camera.name, counter_camera.direction, counter_camera.height, counter_camera.img, counter_camera.width  FROM counter_camera, auth_user_groups, counter_camera_group where auth_user_groups.user_id = %s  and auth_user_groups.group_id = counter_camera_group.group_id and counter_camera_group.camera_id = counter_camera.id and counter_camera.id = %s'


class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


@login_required
def index(request):
    profile = request.user.profile
    camera_list = profile.company.camera_set.all()
    context = {
        'camera_list': camera_list,
    }
    return render(request, 'counter/index.html', context)


@login_required
def detail(request, camera_id):
    cam = request.user.profile.company.camera_set.get(pk=camera_id)
    zones = request.user.profile.company.zone_set.filter(camera_id=cam.id,
                                                         group_id=request.user.profile.company.id)
    timetable = request.user.profile.company.timetable_set.filter(camera_id=cam.id,
                                                                  group_id=request.user.profile.company.id)
    # TODO добавить чтобы зоны были токль о для конкретной организации, то же саме с расписанием
    subprocess.Popen("ffmpeg -i "+cam.url+" -an -vcodec copy -tune zerolatency -t 30 -f flv rtmp://localhost/live/v"+str(cam.id))
    # TODO поменять rtmp на hls
    context = {
        'camera': cam,
        'zones' : zones,
        'timet' : timetable,
    }
    return render(request, 'counter/camera.html', context)


def canvas(request):
    return render(request, 'counter/canvas.html')


# Generic models


class ZoneCreate(CreateView):
    model = Zone
    form_class = ZoneForm
    template_name = 'counter/zone_form.html'
    pk_url_kwarg = 'zone_id'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.camera = get_object_or_404(request.user.profile.company.camera_set.all(), pk=self.kwargs.get('camera_id'))
        return super(ZoneCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.user.profile
        form.instance.group = self.user.profile.company
        form.instance.camera = self.camera
        return super(ZoneCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            zone = self.get_context_data()['zone']
            return reverse('zoneUpdate', kwargs={'camera_id': zone.camera.id,
                                                 'zone_id': zone.id})

    def get_context_data(self, **kwargs):
        context = super(ZoneCreate, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        return context


class ZoneUpdate(UpdateView):
    model = Zone
    form_class = ZoneForm
    template_name = 'counter/zone_form.html'
    pk_url_kwarg = 'zone_id'

    def dispatch(self, request, *args, **kwargs):
        self.camera = get_object_or_404(request.user.profile.company.camera_set.all(), pk=self.kwargs.get('camera_id'))
        get_object_or_404(request.user.profile.company.zone_set, pk=self.kwargs.get('zone_id'))
        return super(ZoneUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            zone = self.get_context_data()['zone']
            return reverse('zoneUpdate', kwargs={'camera_id': zone.camera.id,
                                                 'zone_id': zone.id})

    def get_context_data(self, **kwargs):
        context = super(ZoneUpdate, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        return context


class ZoneOptionCreate(CreateView):
    model = ZoneOption
    form_class = ZoneOptionForm
    pk_url_kwarg = 'zoneop_id'
    template_name = 'counter/zoneoptions_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user.profile
        self.camera = get_object_or_404(request.user.profile.company.camera_set.all(), pk=self.kwargs.get('camera_id'))
        self.zone = self.camera.zone_set.get(pk=self.kwargs.get('zone_id'))
        return super(ZoneOptionCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.zone = self.zone
        form.instance.user = self.user
        form.instance.group = self.user.company
        return super(ZoneOptionCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            zoneop = self.get_context_data()['zoneoption']
            return reverse('zoneopUpdate', kwargs={'camera_id': zoneop.zone.camera_id,
                                                   'zone_id': zoneop.zone.id,
                                                   'zoneop_id': zoneop.id, })
    def get_context_data(self, **kwargs):
        context = super(ZoneOptionCreate, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        return context


class ZoneOptionsUpdate(UpdateView):
    model = ZoneOption
    form_class = ZoneOptionForm
    pk_url_kwarg = 'zoneop_id'
    template_name = 'counter/zoneoptions_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.camera = get_object_or_404(request.user.profile.company.camera_set.all(), pk=self.kwargs.get('camera_id'))
        zone = get_object_or_404(request.user.profile.company.zone_set.all(), pk=self.kwargs.get('zone_id'))
        get_object_or_404(zone.zoneoption_set.all(), pk=self.kwargs.get('zoneop_id'))
        return super(ZoneOptionsUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            zoneop = self.get_context_data()['zoneoption']
            return reverse('zoneopUpdate', kwargs={'camera_id': zoneop.zone.camera_id,
                                                   'zone_id': zoneop.zone.id,
                                                   'zoneop_id': zoneop.id, })

    def get_context_data(self, **kwargs):
        context = super(ZoneOptionsUpdate, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        return context

class TimeTableCreate(CreateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'counter/timetable.html'
    pk_url_kwarg = 'timetable_id'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.camera = get_object_or_404(request.user.profile.company.camera_set.all(), pk=self.kwargs.get('camera_id'))
        return super(TimeTableCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.camera = self.camera
        form.instance.status = 'waiting'
        form.instance.user = self.user.profile
        form.instance.group = self.user.profile.company
        print(form.instance.days)
        if form.instance.days is None:
            form.instance.days = 'NONE'
        return super(TimeTableCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            timetable = self.get_context_data()['timetable']
            return reverse('timetableUpdate', kwargs={'camera_id': timetable.camera.id,
                                                      'timetable_id': timetable.id})

    def zones_as_choices(self):
        zones = []
        for zone in self.user.profile.company.zone_set.filter(camera_id=self.camera.id):
            zos = []
            for zo in zone.zoneoption_set.all():
                zos.append([zo.id, zo.name])
            new_zone = [zone.name, zos]
            zones.append(new_zone)
        return zones

    def get_context_data(self, **kwargs):
        context = super(TimeTableCreate, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        context['form'].fields['options'].choices = self.zones_as_choices()
        return context


class TimeTableUpdate(UpdateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'counter/timetable.html'
    pk_url_kwarg = 'timetable_id'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.camera = get_object_or_404(request.user.profile.company.camera_set.all(), pk=self.kwargs.get('camera_id'))
        get_object_or_404(request.user.profile.company.timetable_set.all(), pk=self.kwargs.get('timetable_id'))
        return super(TimeTableUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            timetable = self.get_context_data()['timetable']
            return reverse('timetableUpdate', kwargs={'camera_id': timetable.camera.id,
                                                      'timetable_id': timetable.id})

    def zones_as_choices(self):
        zones = []
        for zone in self.user.profile.company.zone_set.filter(camera_id=self.camera.id):
            zos = []
            for zo in zone.zoneoption_set.all():
                zos.append([zo.id, zo.name])
            new_zone = [zone.name, zos]
            zones.append(new_zone)
        return zones

    def get_context_data(self, **kwargs):
        context = super(TimeTableUpdate, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        context['form'].fields['options'].choices = self.zones_as_choices()
        return context


class TimeTableDelete(DeleteView):
    model = TimeTable
    pk_url_kwarg = 'timetable_id'
    template_name = 'counter/timetabledelete.html'

    def dispatch(self, request, *args, **kwargs):
        self.camera = get_object_or_404(Camera, pk=self.kwargs.get('camera_id'))
        return super(TimeTableDelete, self).dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            camera = self.get_context_data()['cam']
            return reverse('detail', kwargs={'camera_id': camera.id,
                                             })

    def get_context_data(self, **kwargs):
        context = super(TimeTableDelete, self).get_context_data(**kwargs)
        context['cam'] = self.camera
        return context


def ResultList(request, camera_id):
    # queryset = Results.objects.raw("Select counter_results.id, counter_results.num, counter_results.datetime_start, counter_results.datetime_end, counter_results.direction_Id, counter_results.zone_id_id from counter_results, counter_zoneoption, counter_direction, counter_zone, counter_cuser, counter_camera WHERE counter_results.zone_id_id = counter_zoneoption.id and counter_zoneoption.zone_id = counter_zone.id AND counter_zone.camera_id = "+camera_id+" AND counter_cuser.id = "+str(request.user.id)+" AND counter_results.direction_id = counter_direction.id AND counter_camera.id = "+camera_id+" and counter_zone.user_id ="+str(request.user.id))
    zones = Zone.objects.filter(camera_id=camera_id, group=request.user.profile.company)
    zoneops = ZoneOption.objects.filter(zone__in=zones)
    queryset = Results.objects.filter(zone_id__in=zoneops)
    context = {
        'cam': camera_id,
        'results': queryset,
    }
    return render(request, 'counter/results.html', context)
