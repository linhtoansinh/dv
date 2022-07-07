from unittest import result
from django.shortcuts import render
from django.http import JsonResponse
from .models import HoaDon, CuaHang, HoaDonGiaoHang
from django.db.models import Count, Sum, Case, IntegerField, When, FloatField, F


def graph_total_income(request):
    return render(request, "graphs/graph_total_income.html")

def total_income(request):
    ch_sum = CuaHang.objects.annotate(total=Sum(F('hoadon__tongTien') *
                                                Case(
                                                    When(hoadon__hoadongiaohang__trangThai=True, then=1),
                                                    output_field=FloatField()
                                                )
                                            )).order_by('-total')

    result = []
    for i in ch_sum:
        result.append({'storeid': i.storeID, 'total': i.total})

    return JsonResponse(result, safe=False)

def graph_success(request):
    return render(request, "graphs/graph_success.html")

def success(request):
    ch_success = CuaHang.objects.annotate(success_rate=100*Sum(
                                                            Case(
                                                                When(hoadon__hoadongiaohang__trangThai=True, then=1),
                                                                output_field=IntegerField()
                                                            )
                                                        )/Count('hoadon')
    ).order_by('-success_rate')
    result = []
    for i in ch_success:
        result.append({'storeid': i.storeID, 'success_rate': i.success_rate})
    
    return JsonResponse(result, safe=False)

def graph_ABC_income(request):
    return render(request, "graphs/graph_ABC_income.html")

def ABC_income(request):
    ABC_income = CuaHang.objects.annotate(ABC_income=Sum(F('hoadon__tongTien') *
                                                            Case(
                                                                When(hoadon__hoadongiaohang__trangThai=True, then=3/100),
                                                                output_field=FloatField()
                                                            )
                                                        )
    ).order_by('-ABC_income')
    result = []
    for i in ABC_income:
        result.append({'storeid': i.storeID, 'ABC_income': i.ABC_income})

    return JsonResponse(result, safe=False)
 