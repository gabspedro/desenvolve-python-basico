h_t_m = [40, 37, 45, 40, 40, 48]                     # h_t_m -> Horas Trabalhadas no Mês Inteiro;
                                                     
g_p_h = [n*20 for n in h_t_m if n <= 40]             # g_p_h -> Ganho por Hora | ## Multiplica as horas iguais ou menores do que 40 por 20;
h_e = [((n-40)*25) + 40*20 for n in h_t_m if n > 40] # h_e -> Hora Extra       | ## Subratrai as horas maiores do que 40 por 40 para se obter a hora extra, 
                                                     #                         | ## multiplica a h. extra por 25 e as outras 40 horas por 20 e por fim soma 
                                                     #                         | ## os 2 resultados.
                                                     
p_t = g_p_h + h_e                                    # p -> Pagamento Total    | ## Junta as duas listas sem modificar elas

print(f"Horas Trabalhadas por Semana: {h_t_m}")
print(f"Pagamento Recebido em Dias sem Hora Extra: {g_p_h}")
print(f"Pagamento Recebido em Dias com Hora Extra: {h_e}")
print(f"O Pagamento do Mês foi: {sum(p_t)}")



