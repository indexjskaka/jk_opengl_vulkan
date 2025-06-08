from flask import Flask, request
import requests

app = Flask(__name__)

def verify(id_player):
    url = f"https://inventory.roblox.com/v1/users/{id_player}/items/1/1170214112/is-owned"
    return requests.get(url).json()

@app.route('/verify')
def finalizar():
    id_player = request.args.get("id", "")
    if verify(id_player):
        return '''
        _G.premium_tab:AddSection("Fardamentos")
        dropdown_r_fardamentos = _G.premium_tab:AddDropdown({
            Name = "Jogadores",
            Description = "Selecione o jogador desejado para retirar o fardamento",
            Options = {},
            Default = nil,
            Flag = "dropdown_r_fardamentos",
            Callback = function(Value)
                fardamento_retirar_player_name = Value
            end
        })
        _G.premium_tab:AddButton({"Retirar fardamento", function()
            local a = players_g:FindFirstChild(fardamento_retirar_player_name)
            local b = a.Character or a.CharacterAdded:Wait()
            for _, c in ipairs(b:GetChildren()) do
                if c:IsA("Accessory") then
                    c:Destroy()
                end
            end
        end})
        _G.premium_tab:AddSection("Chat")
        dropdown_chat_fake = _G.premium_tab:AddDropdown({
            Name = "Jogadores",
            Description = "Selecione o jogsdor desejado para retirar o fardamento",
            Options = {},
            Default = nil,
            Flag = "dropdown_chat_fake",
            Callback = function(Value)
                chat_fake_player_name = Value
            end
        })
        _G.premium_tab:AddTextBox({
            Name = "Mensagem",
            PlaceholderText = "Digite a mensagem que o jogador selecionado falará",
            ClearText = false,
            Callback = function(text)
                chat_fake_player_message = text
            end
        })
        _G.premium_tab:AddButton({"Enviar mensagem", function()
            local a = players_g:FindFirstChild(chat_fake_player_name)
            game:GetService("Chat"):Chat(a.Character:WaitForChild("Head"), chat_fake_player_message, Enum.ChatColor.Blue)
        end})
        '''
    else:
        '''
        _G.premium_tab:AddParagraph({"Voce não possui o passe premium, compre-o em nosso servidor do Discord."})
        '''
    
if __name__ = "__main__":
    app.run(host="0.0.0.0", port="8000")
    
