from rest_framework.exceptions import ValidationError


class SupplierNetworkValidator:
    """Проверяет наличие у завода поставщика"""

    def __call__(self, value):
        if value.get('supplier_type') == 0 and value.get('supplier_name'):
            raise ValidationError(
                                  'Завод не может иметь поставщика. '
                                  'Удалите поставщика или укажите тип поставщика - 1 или 2'
                                  )

        if value.get('supplier_name') and value.get('supply_level') is not None:
            if value.get('supply_level') != value['supplier_name'].supply_level + 1:
                raise ValidationError(
                    'Вы указали неверный уровень поставки. '
                    'Пропустите это поле, программа выставляет его автоматически'
                )

        if value.get('supply_level') is None and value.get('supplier_name') is None and value.get('supplier_type') is None:
            raise ValidationError(
                'Чтобы создать поставщика, нужно указать его тип. '
                'Если вы завод, укажите тип поставщика - 0'
            )

        if value.get('supplier_type') != 0 and value.get('supply_level') is None and value.get('supplier_name') is None:
            raise ValidationError(
                'Поле поставщика не может быть пустым. '
                'Если вы завод, укажите тип поставщика - 0'
            )

        if value.get('supplier_type') == 0 and value.get('supply_level') != 0 and value.get('supply_level') is not None:
            raise ValidationError(
                'Вы выбрали тип сети завод - 0. '
                'В цепочке поставок вы можете иметь только уровень - 0. '
                'Не указывайте уровень и поставщика, либо укажите вашего поставщика и правильный тип поставщика'
                '1. Не указывайте уровень и поставщика, либо укажите уровень в цепочке поставки - 0. '
                '2. Если не вы являетесь заводом, укажите вашего поставщика и тип сети.'
            )

        if value.get('supplier_type') is None and value.get('supply_level') != 0 and value.get('supplier_name'):
            raise ValidationError(
                'Для создания поставщика укажите тип вашей сети.'
            )