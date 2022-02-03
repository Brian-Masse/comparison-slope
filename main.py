import pygame
import random 
import math
import sys
sys.path.append( "." ) 
from independent_work.colors import color

pygame.init()

width = 1700
height = 500

graphing_width = 500
graphing_height = 200
graph_pos = ( 10, 0 )

display = pygame.display.set_mode((width, height))
running = True

graph_color = (10,10,10)
end_method_line = (66, 166, 99)
regression_method_line = (109, 227, 178)

class Graph:
    def __init__(self, size, pos, rand):
        self.size = size
        self.pos = pos
        self.series = []
        self.rand = rand
    
    def calculate_points(self):
        self.series = []
        series1 = []
        for x in range(0, graphing_width):
            rand = self.rand(x)
            series1.append( ( x, rand ) )
        self.series.append( series1 )   

    def render_points(self):
        for series in self.series:
            for point in series:
                translated_point = ( point[0] + self.pos[0], height - ( point[1] + self.pos[1] + 20))
                pygame.draw.circle( display, graph_color, translated_point, 2 )
    
    def frame(self):
        pygame.draw.line( display, graph_color, ( self.pos[0], height - self.pos[1] ), ( self.pos[0] + self.size[0], height - self.pos[1] )  )
        pygame.draw.line( display, graph_color, ( self.pos[0] + self.size[0], height - (self.pos[1]) ), ( self.pos[0] + self.size[0], height - (self.pos[1]+ self.size[1] )) )
        pygame.draw.line( display, graph_color, ( self.pos[0] + self.size[0], height - (self.pos[1]+ self.size[1]) ), (self.pos[0], height - (self.pos[1] + self.size[1])) )
        pygame.draw.line( display, graph_color, (self.pos[0], height - (self.pos[1] + self.size[1])), (self.pos[0], height - self.pos[1]  ))


    def render_best_fit(self, series):
    
        start, end = self.calculate_line_method1(series)
        pygame.draw.line( display, regression_method_line, start, end, 2 )

        start, end = self.calculate_line_method2(series)
        pygame.draw.line( display, end_method_line, start, end, 2 )

    def calculate_line_method2(self, series):
        y_initial = 0
        y_final = 0
        length = len(self.series[series])
        for i in range(0, 5):
            y_initial += self.series[series][i][1]
            y_final += self.series[series][ length - 1 - i][1]

        y_initial /= 5
        y_final /= 5

        start = (self.pos[0], height - (y_initial + self.pos[1]))
        end = (graphing_width +self.pos[0], height - (y_final + self.pos[1]))
        return (start, end)

    def calculate_line_method1(self, series):
        x = 0
        y = 0
        for points in self.series[series]:
            x += points[0]
            y += points[1]
        x /= len(self.series[series])
        y /= len(self.series[series])

        slope = 0
        for point in self.series[series]:
            delta_x = ( point[0] - x )
            delta_y = ( point[1] - y )
            slope += (delta_y / delta_x)
        slope /= len(self.series[series])
        y_intercept = self.series[series][0][1] - slope * ( self.series[series][0][0] )

        y_final = slope * graphing_width + y_intercept

        start = (self.pos[0], height - (y_intercept + self.pos[1]))
        end = (graphing_width + self.pos[0], height - (y_final + self.pos[1]))
        return (start, end)

delta = graphing_height / 2

def calculate_rand(x):    
    return random.uniform( x *0.2, (x * 0.2) + delta)
    
def calculate_rand2(x):
    return random.uniform( math.cos(x * 0.05) * 20, int((math.cos(x * 0.05) * 20) + delta ) )

def calculate_rand3(x):
    return random.uniform( 0,  graphing_height / 2 )

def calculate_rand4(x):    
    return random.uniform( x * 0.8, (x * 0.8) + delta )

def calculate_rand5(x):    
    return random.uniform( 0.005 * ((x - 250) * (x - 250)), 0.005 * ((x - 250) * (x - 250)) + delta )
    



graph = Graph(( graphing_width, graphing_height ), (10, 20), calculate_rand)
graph2 = Graph(( graphing_width, graphing_height ), (550, 20), calculate_rand2)
graph3 = Graph(( graphing_width, graphing_height * 1.2 ), (10, 250), calculate_rand3)
graph4 = Graph(( graphing_width, graphing_height * 1.2 ), (550, 250), calculate_rand4)
graph5 = Graph(( graphing_width, graphing_height * 2.3 ), (1100, 20), calculate_rand5)

graphs = [ graph, graph2, graph3, graph4, graph5 ]

back = pygame.image.load( "./independent_work/comparison-slope/background/back.jpg")
back = pygame.transform.scale( back, ( width, height ) )
display.blit( back, (0, 0) )

for graph in graphs:
    graph.frame()
    graph.calculate_points()
    graph.render_points()

    for i in range(0, 10):
        graph.calculate_points()
        graph.render_best_fit(0)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

    # display.fill( ( 255, 255, 255 ) )

    # for graph in graphs:
    #     graph.calculate_points()
    #     graph.render_points()

    #     for i in range(0, 10):
    #         graph.calculate_points()
    #         graph.render_best_fit(0)
    
pygame.quit()


