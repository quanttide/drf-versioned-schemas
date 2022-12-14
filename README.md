# `drf-versioned-schemas`

Versioned schemas for Django REST Framework.

## Installation

```shell
pip install drf-versioned-schemas
```

## Usage

遵循[量潮RESTful API规范](https://github.com/quanttide/quanttide-restful-api-specification)
的[版本管理的领域模型](https://github.com/quanttide/quanttide-restful-api-specification/tree/master/versioned_schemas)
的领域模型和API。

### 定义模型类

把计划版本管理的模型分为不可变部分和可变部分，其中：
- 不可变部分继承`VersionedModel`类。
- 可变部分继承`ModelVersion`类，关联上述模型的字段的`related_name`设置成`versions`。

`ModelVersion`和`VersionedModel`增加了`is_active`字段，并把`delete`定义为标记`is_active=False`。

```python
# models.py
import uuid
from django.db import models
from drf_versioned_schemas.models import VersionedModel, ModelVersion


class ExampleModel(VersionedModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='ID')
    name = models.CharField(max_length=128, unique=True, verbose_name='名称')


class ExampleModelVersion(ModelVersion):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='版本ID')
    model = models.ForeignKey(ExampleModel, related_name='versions', on_delete=models.CASCADE, verbose_name='数据模型')
    version = models.CharField(max_length=64, verbose_name='版本')
    title = models.CharField(max_length=128, verbose_name='标题')
    created_at = models.DateTimeField(verbose_name='版本创建时间')
```

### 定义序列化类

使用普通的序列化类定义`ModelVersion`子类的序列化和反序列化行为。
使用`VersionedModelSerializer`定义完整序列化和反序列化行为，在`VersionMeta`配置如下字段：
- `version_serializer`: 上述用作模型版本的序列化类。
- `version_field`: 版本字段，比如`version`。
- `version_related_name`: 版本模型和模型的关联名称，比如`versions`。
- `version_field_mapping`: 序列化时用作规定模型字段转换的方式，比如把模型版本`created_at`定义为模型`updated_at`。

```python
# serializers.py
from rest_framework import serializers
from drf_versioned_schemas.serializers import VersionedModelSerializer

from .models import *


class ExampleModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModelVersion
        exclude = ['id', 'model', 'is_active']


class ExampleModelSerializer(VersionedModelSerializer):
    class Meta:
        model = ExampleModel
        exclude = ['is_active']

    class VersionMeta:
        version_serializer = ExampleModelVersionSerializer
        version_field = 'version'
        version_related_name = 'versions'
        version_field_mapping = {'created_at': 'updated_at'}
```

### 定义视图类

依照官方实现即可。


### 定义路由类

依照官方实现即可。

## License

[BSD 3-Clause License](LICENSE)
