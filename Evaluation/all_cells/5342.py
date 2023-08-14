# definimos parámetros generales
C = 10
D = 784
N = size(x_ent)[1] # número de puntos de datos disponibles para entrenar

# definimos los parámetros que podemos afinar (excepto el número de capas ocultas)
H = 256
M = 10 # número de mini-montones
NM = N/M # número de datos por mini-monton
alpha = 0.1 # taza de aprendizaje
lambda = 0.0001 # fuerza de regularización
epocas = 30

# inicializamos las neuronas y sus sesgos
Wh = (rand(D,H) - 0.5)*0.01
bh = (rand(1,H) - 0.5)*0.01
Wo = (rand(H,C) - 0.5)*0.01
bo = (rand(1,C) - 0.5)*0.01

# inicializamos el arreglo para visualizar la pérdida
Js = zeros(epocas*M)

# ciclo para mostrar los datos más de una epoca
for ep = 1:epocas

    # generando indices aleatorios (es importante aleatorizar los datos en cada epoca)
    x_ind_aleat = sample(1:N, N, replace = false)

    # ciclo para iterar sobre los mini-montones de datos
    for mm = 0:M-1
       
        # accediendo los datos del mini-montón de datos actual
        mini_x = x_ent[x_ind_aleat[floor(Int,(mm*NM)+1:(mm*NM)+NM)],:]
        mini_y = y_ent[x_ind_aleat[floor(Int,(mm*NM)+1:(mm*NM)+NM)],:]

        # forward pass
        h = tanh(mini_x*Wh + bh.*ones(size(tanh(mini_x*Wh))))
        v = h*Wo + bo.*ones(size(h*Wo))
        y_hat = exp(v)./sum(exp(v),2)

        # calculando la pérdida        
        J = 0
        for n = 1:NM
            J = J + -log(y_hat[floor(Int,n),floor(Int,mini_y[floor(Int,n),:])+1])
        end        
        Js[((ep-1)*M) + mm+1,:] = J/NM + lambda*(0.5*sum(Wh.^2) + 0.5*sum(Wo.^2))
        
        # generando e_correcto
        e_correcto = zeros(size(y_hat))
        for n = 1:NM
            e_correcto[floor(Int,n),floor(Int,mini_y[floor(Int,n),:])+1] = 1
        end
        
        # backward pass
        dJ_dv = (y_hat .- e_correcto)./NM
        dJ_dWo = h'*dJ_dv + lambda*Wo
        dJ_dbo = sum(dJ_dv,1)
        
        dJ_dh = (ones(size(h)) .- tanh(h).^2).*(dJ_dv*Wo')
        dJ_dWh = mini_x'*dJ_dh + lambda*Wh
        dJ_dbh = sum((dJ_dh),1)
        
        # actualizando los parámetros
        Wo = Wo - alpha*dJ_dWo
        bo = bo - alpha*dJ_dbo
        Wh = Wh - alpha*dJ_dWh
        bh = bh - alpha*dJ_dbh      
        
    end 

    # midiendo la precisión con los datos de entrenamiento
    h = tanh(x_ent*Wh + bh.*ones(size(tanh(x_ent*Wh))))
    v = h*Wo + bo.*ones(size(h*Wo))
    y_hat = exp(v)./sum(exp(v),2)
    y_max = findmax(y_hat',1)
    y_max_ind = y_max[2] - range(0,N)'*C    
    print("------------------------------------------------------------------------------")
    print("\nÉpoca: ", ep)
    print("\nPrecisión con los datos de entrenamiento:",sum(y_max_ind .== (y_ent .+ ones(size(y_ent)))')/N, "\n")

    # midiendo la precisión con los datos de validación
    h = tanh(x_val*Wh + bh.*ones(size(tanh(x_val*Wh))))
    v = h*Wo + bo.*ones(size(h*Wo))
    y_hat = exp(v)./sum(exp(v),2)
    y_max = findmax(y_hat',1)
    y_max_ind = y_max[2] - range(0,length(y_val))'*C    
    print("Precisión con los datos de validación:",sum(y_max_ind .== (y_val .+ ones(size(y_val)))')/length(y_val), "\n")

    
end

using PyPlot
plot(linspace(0,epocas,length(Js)),Js)
xlabel("Época")
ylabel("Pérdida")