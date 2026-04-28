
## Модели
- `Tag` — название тега
- `Scope` — связь Article↔Tag с `is_main` (through)
- `Article` — `scopes = ManyToManyField(Tag, through=Scope, related_name='scopes')`

## Админка
- `TagAdmin` — CRUD тегов
- `ArticleAdmin` с `ScopeInline` 
- **Валидация**: ровно 1 `is_main=True` (`ScopeInlineFormset.clean`)

## Views + Шаблоны
- `/` — список статей (`news/index.html`)
- `/<id>/` — детальная с **scopes** (`news/detail.html`)
- **Сортировка**: main первый (`-is_main`), остальные алфавитно (`tag__name`)

## Тестирование
- http://127.0.0.1:8000/admin/ 
- http://127.0.0.1:8000/1/ 
