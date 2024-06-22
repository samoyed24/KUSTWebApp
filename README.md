# KUSTWebApp

### 启动后端：
> uvicorn main:app --host 0.0.0.0 --port 80 --reload（在局域网上启动）

### 启动前端：
> 首次启动：npm install
> 启动开发服务器np：npm run dev

### alembic基本操作
> 初始化 alembic init alembic
> 
> 生成迁移脚本 alembic revision --autogenerate -m (description)
>
> 执行迁移 alembic upgrade head
