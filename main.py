from banco import Banco
from errors import (
    BancoError,
    ValorInvalidoError,
    SaldoInsuficienteError,
    ContaNaoEncontradaError,
    NomeObrigatorioError,
    OpcaoInvalidaError,
    OperacaoCanceladaError,
    LimiteSaqueExcedidoError,
    LimiteTransferenciaExcedidoError,
    ContaJaExisteError,
)


def mostrar_menu():
    print("\n=== Banco do Brasil ===")
    print("1 - Criar nova conta")
    print("2 - Listar contas")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Transferir")
    print("6 - Alterar nome do titular")
    print("0 - Sair")


def main():
    banco = Banco("Banco do Brasil")

    while True:
        try:
            mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                print("\nSaindo... Obrigado por usar o Banco do Brasil!")
                break

            if opcao == "1":
                nome = input("Nome do titular: ").strip()
                if not nome:
                    raise NomeObrigatorioError("O nome do titular não pode ser vazio.")

                saldo_str = input("Saldo inicial (vazio para 0): ").strip()

                if saldo_str == "0":
                    raise ValorInvalidoError(
                        "O saldo inicial não pode ser zero. Deixe em branco para usar o padrão."
                    )

                saldo = float(saldo_str) if saldo_str else 0.0
                conta = banco.criar_conta(nome, saldo)

                print("\n[SUCESSO] Conta criada com sucesso!")
                conta.exibir_resumo()

            elif opcao == "2":
                banco.listar_contas()

        
            elif opcao == "3":
                num_str = input("Número da conta (vazio para cancelar): ").strip()
                if not num_str:
                    raise OperacaoCanceladaError("Depósito cancelado pelo usuário.")

                num = int(num_str)
                conta = banco.buscar_conta_por_numero(num)

                valor_str = input("Valor do depósito: R$ ").strip()
                if not valor_str:
                    raise OperacaoCanceladaError("Depósito cancelado (sem valor informado).")

                valor = float(valor_str)
                conta.depositar(valor)
                print("\n[SUCESSO] Depósito realizado!")
                conta.exibir_resumo()

    
            elif opcao == "4":
                num_str = input("Número da conta (vazio para cancelar): ").strip()
                if not num_str:
                    raise OperacaoCanceladaError("Saque cancelado pelo usuário.")

                num = int(num_str)
                conta = banco.buscar_conta_por_numero(num)

                valor_str = input("Valor do saque: R$ ").strip()
                if not valor_str:
                    raise OperacaoCanceladaError("Saque cancelado (sem valor informado).")

                valor = float(valor_str)
                conta.sacar(valor)
                print("\n[SUCESSO] Saque realizado!")
                conta.exibir_resumo()

            
            elif opcao == "5":
                num_origem_str = input("Número da conta ORIGEM (vazio para cancelar): ").strip()
                if not num_origem_str:
                    raise OperacaoCanceladaError("Transferência cancelada (sem conta de origem).")

                num_origem = int(num_origem_str)
                conta_origem = banco.buscar_conta_por_numero(num_origem)

                num_destino_str = input("Número da conta DESTINO (vazio para cancelar): ").strip()
                if not num_destino_str:
                    raise OperacaoCanceladaError("Transferência cancelada (sem conta de destino).")

                num_destino = int(num_destino_str)
                conta_destino = banco.buscar_conta_por_numero(num_destino)

                valor_str = input("Valor da transferência: R$ ").strip()
                if not valor_str:
                    raise OperacaoCanceladaError("Transferência cancelada (sem valor informado).")

                valor = float(valor_str)

                conta_origem.transferir(conta_destino, valor)

                print("\n[SUCESSO] Transferência realizada!")
                print("Conta ORIGEM:")
                conta_origem.exibir_resumo()
                print("Conta DESTINO:")
                conta_destino.exibir_resumo()

    
            elif opcao == "6":
                num_str = input("Número da conta (vazio para cancelar): ").strip()
                if not num_str:
                    raise OperacaoCanceladaError("Alteração de nome cancelada pelo usuário.")

                num = int(num_str)
                conta = banco.buscar_conta_por_numero(num)

                novo_nome = input("Novo nome do titular: ").strip()
                if not novo_nome:
                    raise NomeObrigatorioError("O novo nome do titular não pode ser vazio.")

                conta.titular.nome = novo_nome
                print("\n[SUCESSO] Nome do titular alterado!")
                conta.exibir_resumo()

            else:
                
                raise OpcaoInvalidaError(f"A opção '{opcao}' não é válida. Tente novamente.")

        

        except (ValueError, TypeError):
            print("\n[ERRO] Valor numérico inválido. Tente novamente.")

        except ValorInvalidoError as e:
            print(f"\n[ERRO DE VALOR] {e}")

        except SaldoInsuficienteError as e:
            print(f"\n[ERRO DE SALDO] {e}")

        except ContaNaoEncontradaError as e:
            print(f"\n[ERRO] Conta não encontrada: {e}")

        except NomeObrigatorioError as e:
            print(f"\n[ERRO DE DADOS] {e}")

        except OpcaoInvalidaError as e:
            print(f"\n[AVISO] {e}")

        except OperacaoCanceladaError as e:
            print(f"\n[INFO] {e}")

        except LimiteSaqueExcedidoError as e:
            print(f"\n[ERRO DE LIMITE] {e}")

        except LimiteTransferenciaExcedidoError as e:
            print(f"\n[ERRO DE LIMITE] {e}")

        except ContaJaExisteError as e:
            print(f"\n[ERRO DE CONTA] {e}")

        except BancoError as e:
            print(f"\n[ERRO DE SISTEMA] {e}")

        except KeyboardInterrupt as e:
            print(f"\n[ERRO] {e.__class__}: Operação interrompida pelo usuário.")
            print("Se quiser sair do sistema, escolha a opção 0 no menu.")

        else:
        
            if opcao not in {"1", "3", "4", "5", "6"}:
                print("Operação realizada com sucesso (sem erros).")

        finally:
            print("Retornando ao menu principal...")


if __name__ == "__main__":
    main()
