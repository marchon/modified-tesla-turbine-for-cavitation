#!/usr/bin/env python3
"""
Flow Path Animation Generator
Creates a sequence of frames + animated GIF showing progressive flow through the device.

This simulates:
1. Tangential inlet injection
2. Spiral development between platters
3. Central convergence + HVAT conditioning
4. Acceleration through Venturi nozzle

Requires: matplotlib + pillow (PIL)
Run: python3 python/generate_flow_animation.py
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
from PIL import Image
import glob

OUT_DIR = "illustrations/flow_frames"
os.makedirs(OUT_DIR, exist_ok=True)

def generate_flow_frames(n_frames=24):
    """Generate frames showing flow development."""
    print(f"Generating {n_frames} flow animation frames...")
    
    for frame in range(n_frames):
        progress = frame / (n_frames - 1)  # 0 to 1
        
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(-70, 70)
        ax.set_ylim(-45, 45)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f"Flow Development — Frame {frame+1}/{n_frames}\n"
                     "Tangential Inlets → Spiral Conditioning → HVAT → Cavitation Nozzle", fontsize=10)
        
        # Housing outline
        housing = Circle((0, 0), 52, fill=False, color='#7f8c8d', linewidth=2, linestyle='--')
        ax.add_patch(housing)
        
        # Platters (simplified)
        for y in np.linspace(-22, 22, 7):
            ax.plot([-42, 42], [y, y], color='#2c3e50', linewidth=1.5, alpha=0.6)
        
        # Progressive flow particles / arrows
        n_inlets = 6
        for i in range(n_inlets):
            angle = np.radians(i * 60 + 30)
            # Inlet position
            ix = 48 * np.cos(angle)
            iy = 48 * np.sin(angle)
            
            # How far this inlet's flow has progressed (staggered by inlet)
            inlet_progress = max(0, min(1, (progress * 1.3) - (i * 0.08)))
            
            if inlet_progress > 0.05:
                # Spiral inward path
                spiral_r = 48 - (inlet_progress * 38)
                spiral_angle = angle - (inlet_progress * 2.8)  # spiral inward
                
                fx = spiral_r * np.cos(spiral_angle)
                fy = spiral_r * np.sin(spiral_angle)
                
                # Draw arrow or particle
                ax.annotate('', xy=(fx, fy), xytext=(ix, iy),
                            arrowprops=dict(arrowstyle='->', color='#e74c3c', 
                                           lw=1.8, alpha=0.7 + 0.3*inlet_progress))
        
        # Central HVAT zone (activates mid-progress)
        if progress > 0.35:
            hvat_alpha = min(0.9, (progress - 0.35) * 2)
            ax.add_patch(Circle((0, 0), 14, fill=True, facecolor='#8e44ad', alpha=0.25 * hvat_alpha))
            ax.text(0, 0, "HVAT\nConditioning", ha='center', va='center', fontsize=7, 
                   color='#6c3483', alpha=hvat_alpha)
        
        # Final nozzle acceleration (late progress)
        if progress > 0.65:
            nozzle_alpha = min(0.95, (progress - 0.65) * 3)
            ax.annotate('', xy=(42, 0), xytext=(22, 0),
                        arrowprops=dict(arrowstyle='->', color='#27ae60', lw=3, alpha=nozzle_alpha))
            ax.text(32, 6, "Cavitation\nJet", ha='center', va='center', fontsize=7, 
                   color='#1e8449', alpha=nozzle_alpha)
        
        # Stage labels
        ax.text(-55, 38, "1. Tangential\n   Inlets", fontsize=8, color='#c0392b')
        ax.text(-10, -38, "2. Multi-channel\n   Spiral", fontsize=8, color='#2c3e50')
        if progress > 0.4:
            ax.text(18, 32, "3. HVAT\n   Straightening", fontsize=8, color='#8e44ad')
        if progress > 0.7:
            ax.text(38, -12, "4. Venturi\n   Acceleration", fontsize=8, color='#27ae60')
        
        plt.tight_layout()
        frame_path = os.path.join(OUT_DIR, f"flow_frame_{frame:03d}.png")
        plt.savefig(frame_path, dpi=120, bbox_inches='tight', facecolor='white')
        plt.close(fig)
    
    print(f"  → {n_frames} frames saved to {OUT_DIR}/")

def create_gif():
    """Combine frames into an animated GIF."""
    print("Creating animated GIF...")
    frames = sorted(glob.glob(os.path.join(OUT_DIR, "flow_frame_*.png")))
    if not frames:
        print("No frames found!")
        return
    
    images = [Image.open(f) for f in frames]
    
    gif_path = "illustrations/flow_path_animation.gif"
    images[0].save(
        gif_path,
        save_all=True,
        append_images=images[1:],
        duration=120,  # ms per frame
        loop=0
    )
    print(f"  → Animated GIF saved to {gif_path}")

if __name__ == "__main__":
    generate_flow_frames(n_frames=20)
    create_gif()
    print("\nFlow path visualization complete (frames + GIF).")