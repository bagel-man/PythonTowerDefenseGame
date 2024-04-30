import pygame as pg
from pygame.math import Vector2
import math

class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.angle = 0
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.move()
        self.rotate()

    def move(self):
        # define target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # enemy is at end of path, it has served its purpose and must be eliminated
            self.kill()
        # calculate distance to target hehe
        dist = self.movement.length()
        # check if remaining is greater that speed
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1

    def rotate(self):
        # calculate distance to next waypoint
        dist = self.target - self.pos
        print(dist)
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        # rotate image and rectangle
        # self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        print(self.angle)
        if self.angle <= -90:
            self.image = pg.transform.flip(self.original_image, True, False)
        elif dist[0]+dist[1] != 0:
            self.image = pg.transform.flip(self.original_image, False, False)