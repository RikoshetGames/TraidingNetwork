sup_name = models.CharField(max_length=200, verbose_name='Название')
supplier_type = models.IntegerField(choices=supplier_type_list, verbose_name='Уровень сети', default=0)


company_name = models.CharField(max_length=200, verbose_name='Название')
seller_type = models.IntegerField(choices=seller_type_list, verbose_name='Уровень сети', default=0)