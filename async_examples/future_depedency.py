from asyncio import Future, run, create_task, sleep


async def corrotina1(future: Future):
    print("Tarefa 1 iniciada.")
    await sleep(2)
    future.set_result("Resultado da Tarefa 1")
    print("Tarefa 1 finalizada")

async def corrotina2(future: Future):
    print("Tarefa 2 iniciada, aguardando o futuro.")
    result = await future
    print(f"Tarefa finalizda com o resultado: {result}")

async def main():
    future = Future()
    #cria as tarefas que referênciam o mesmo objeto feture
    #nesse contexto, a corrtina 2 depende do resultado da corrotina1
    #porém mesmo assim, as duas rodam simultânemamente
    task1 = create_task(corrotina1(future))
    task2 = create_task(corrotina2(future))

    #roda as duas tasks concorrentemente (simultaneamente)
    await task1
    await task2

run(main())
