class Stats():
    #статистика

    def __init__(self):
        #инициализация статистики
        self.reset_stats()
        self.run_game = True
    
    
    def reset_stats(self):
        #статистика, изменяющаяся во время игры
        
        self.sokol_life = 2