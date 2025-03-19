import time
import asyncio
import pandas as pd


#definindo função assincrona para pegar api
async def corrotina(task_name, time_await):
    print(f"Iiniciando a tarefa {task_name}")
    await asyncio.sleep(time_await)
    print(f"Finalizando a tarefa {task_name}")

async def main():
    task1 = asyncio.create_task(corrotina("Criar conexão com o banco de dados", 2))
    task2 = asyncio.create_task(corrotina("Puxar api do google", 1))
    """
        Com o create_task criamos duas tarefas que executam concorrentemente
        onde agora as duas são aguardadas. Sem isso elas esperam que uma execute para depois terminar
    """
    df_funcionarios = pd.DataFrame({
        "Nomes": [
            "Alexander Alcantara Linhares",
            "Antonio roberto da cunha",
            "Roberto Carlos"
        ],
        "Notas": [
            6,
            9,
            8.5
        ]
    })

    for nome in df_funcionarios.Nomes:
        print(f"Nome dos funcionários {nome}")
        await task1
    
    await task2
    print("Finalizando código")

async def app():
    print("Iniciando app")
    async_main = asyncio.create_task(main())
    print("Renderizando aplicativo")
    await async_main

asyncio.run(app())