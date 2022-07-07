import random
from django.core.management.base import BaseCommand

from vis_app.models import CuaHang, HoaDon, HoaDonGiaoHang


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='số đơn hàng cần tạo')

    def handle(self, *args, **options):
        list_cua_hang = []
        # CuaHang.objects.all().delete()
        # HoaDon.objects.all().delete()
        # HoaDonGiaoHang.objects.all().delete()
        # for i in range(10):
        #     cua_hang = CuaHang.objects.create(
        #         storeID=str(i),
        #         loaiCH=random.choice(CuaHang.THU_PHI)[0]
        #     )
        #     list_cua_hang.append(cua_hang)
        #     cua_hang.save()
        #     print(cua_hang.id)

        amount = options['amount'] if options['amount'] else 50
        for i in range(0, amount):
            ch_id = random.randint(51,60)
            ch = CuaHang.objects.only('id').get(id=ch_id)
            hoa_don = HoaDon.objects.create(
                maHD=str(i),
                tongTien=random.randint(50,1000)*1000,
                # account_CH=random.randint(0,9),
                account_CH = ch,
            )
            hoa_don.save()

            hd = HoaDon.objects.only('id').get(id=hoa_don.id)
            hoa_don_gh = HoaDonGiaoHang.objects.create(
                maHD=hd,
                trangThai=True if random.randint(1, 2) == 1 else False
            )
            hoa_don_gh.save()

        self.stdout.write(self.style.SUCCESS('Okay'))