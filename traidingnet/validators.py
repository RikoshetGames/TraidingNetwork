from rest_framework.exceptions import ValidationError


class SupplierNetworkValidator:
    """Проверяет наличие у завода поставщика"""

    def __call__(self, value):
        if value.get('seller_type') == 0 and value.get('supplier_name'):
            raise ValidationError(
                                  'Компания типа "Завод" не может иметь поставщика. '
                                  'Удалите поставщика или укажите тип компании - 1 или 2'
                                  )

        if value.get('seller_type') != 0 and value.get('supply_level') == 0 and value.get('supplier_name') != 0:
            raise ValidationError('На нулевом уровне поставки может находиться только компания типа "завод". '
                                  'Выберете корректный тип компании или удалите поставщика.'
                                  )

        if value.get('supplier_name') and value.get('supply_level') is not None:
            if value.get('supply_level') != value['supplier_name'].supply_level + 1:
                raise ValidationError(
                    'Вы указали неверный уровень поставки. '
                    'Пропустите это поле, программа выставляет его автоматически.'
                )

        if value.get('supply_level') is None and value.get('supplier_name') is None and value.get('seller_type') is None:
            raise ValidationError(
                'Чтобы создать поставщика, нужно указать его тип. '
                'Если вы завод, укажите тип поставщика - 0'
            )

        if value.get('seller_type') != 0 and value.get('supply_level') is None and value.get('supplier_name') is None:
            raise ValidationError(
                'Поле поставщика не может быть пустым. '
                'Если вы завод, укажите тип поставщика - 0.'
            )

        if value.get('seller_type') == 0 and value.get('supply_level') != 0 and value.get('supply_level') is not None:
            raise ValidationError(
                'Вы выбрали тип компании "завод" - 0. '
                'В цепочке поставок вы можете иметь только уровень - 0. '
                'Не указывайте уровень и тип компании, либо укажите вашего поставщика и правильный тип компании.'
            )

        if value.get('seller_type') is None and value.get('supply_level') != 0 and value.get('supplier_name'):
            raise ValidationError(
                'Для создания поставщика укажите тип вашей компании.'
            )

        if value.get('supply_level') == 0 and value.get('seller_type') != 0:
            raise ValidationError('На нулевом уровне поставки может быть только завод. '
                                  'Если вы являетесь заводом, укажите тип компании - 0.'
                                  )

        if value.get('seller_type') != 0 and value.get('supply_level') != 0 and value.get('supplier_name') is None:
            raise ValidationError('Вы указали тип сети, не являющегося заводом. '
                                  'Если вы являетесь не заводом, укажите вашего поставщика.'
                                  )

        if value.get('seller_type') == 0 and value.get('debt') is not None:
            raise ValidationError('У завода не может быть задолженности. '
                                  'Если вы являетесь заводом, оставьте поле задолженности пустым.'
                                  )
