from asyncio import Future, sleep, create_task, run

"""
    o objeto Future não possui valor definido,
    porém pode ser definido no futuro
"""
#a corrotina é uma função async que possui o parâmetro future
async def corrotina1(future: Future):
    print("Início.")
    #aguarda temporariamente a execução das tarefas
    await sleep(2)
    #definimos agora o valor do objeto future
    future.set_result("Fim.")

async def main():
    future = Future()
    create_task(corrotina1(future))
    result = await future
    print(result)

run(main())