

local UserInputService = game:GetService("UserInputService")
local Players = game:GetService("Players")
local Player = Players.LocalPlayer
local Character = Player.Character or Player.CharacterAdded:Wait()
local Humanoid = Character:WaitForChild("Humanoid")
local RunAnim = script:WaitForChild("RunAnim")
local punchAnim = Instance.new("Animation")
punchAnim.AnimationId = "rbxassetid://70641360701114"
local runAnimPlay = Humanoid:LoadAnimation(RunAnim)
local punchAnimPlay = Humanoid:LoadAnimation(punchAnim)
local isPlayingRun = false
local isPunching = false
local db = true 
local punchanims = {
	'70641360701114',
	'138818396742168',
	'136841104851133',
	'131407614582550'}

local function onCharacterAdded(character)
	Character = character
	Humanoid = character:WaitForChild("Humanoid")
	runAnimPlay = Humanoid:LoadAnimation(RunAnim)
	punchAnimPlay = Humanoid:LoadAnimation(punchAnim)
end
Player.CharacterAdded:Connect(onCharacterAdded)
UserInputService.InputBegan:Connect(function(input, gameProcessed)
	if gameProcessed then return end

	if input.KeyCode == Enum.KeyCode.LeftShift and isPunching == false	then
		Humanoid.WalkSpeed = 25
		if not isPlayingRun then
			isPlayingRun = true
			runAnimPlay:Play()
		end
	end
end)

UserInputService.InputEnded:Connect(function(input, gameProcessed)
	if input.KeyCode == Enum.KeyCode.LeftShift then 
		Humanoid.WalkSpeed = 12
		if isPlayingRun then
			isPlayingRun = false
			runAnimPlay:Stop()
		end
	end
end)

local index = 0
UserInputService.InputBegan:Connect(function(input, gameProcessed)
	if gameProcessed then return end

	if db and input.KeyCode == Enum.KeyCode.E and not isPlayingRun then
		db = false
		lastKeyPress = tick() 

		
		index += 1
		if index > #punchanims then
			index = 1
		end
		print(index)
		print(punchanims[index])
		punchAnim.AnimationId = `rbxassetid://{punchanims[index]}`
		local punchAnimPlay = Humanoid:LoadAnimation(punchAnim)
		punchAnimPlay:Play()
		punchAnimPlay.Stopped:Connect(function()
			db = true
		end)
	end
end)
task.spawn(function()
	while true do
		wait(0.1)
		if tick() - lastKeyPress >= resetTime then
			index = 1
			print("Index reset to 1 due to inactivity")
			lastKeyPress = tick() 
		end
	end
end)
