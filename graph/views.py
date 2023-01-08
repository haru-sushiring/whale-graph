from django.http import HttpResponse

import os
from dotenv import load_dotenv

# db_urlの読み込み
load_dotenv()

import pandas as pd
import psycopg2

# def index(request):
#   return render(request, 'index.html')

from django.views.generic import TemplateView
from . import models
from . import graph


class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        # qs = models.Whale.objects.all()
        qs = models.Whale.objects.order_by('timestamp')
        #print(qs)
        x  = [x.timestamp for x in qs]
        y  = [y.amount for y in qs]
        z  = [z.price for z in qs]
        judge = 'sum'
        sum_graph = graph.Plot_Graph(x,y,z,judge)

        qs = models.Whale.objects.order_by('timestamp').filter(move='buy')
        x  = [x.timestamp for x in qs]
        y  = [y.amount for y in qs]
        z  = [z.price for z in qs]
        judge = 'buy'
        buy_graph = graph.Plot_Graph(x,y,z,judge)

        qs = models.Whale.objects.order_by('timestamp').filter(move='sell')
        x  = [x.timestamp for x in qs]
        y  = [y.amount for y in qs]
        z  = [z.price for z in qs]
        judge = 'sell'
        sell_graph = graph.Plot_Graph(x,y,z,judge)

        context = super().get_context_data(**kwargs)
        context['sum'] = sum_graph
        context['buy'] = buy_graph
        context['sell'] = sell_graph
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
