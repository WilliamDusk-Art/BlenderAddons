keyconfig_version = (4, 0, 36)
keyconfig_data = \
[("3D View",
  {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
  {"items":
   [("view3d.cursor3d", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True}, None),
    ("transform.translate",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True},
     {"properties":
      [("cursor_transform", True),
       ("release_confirm", True),
       ],
      },
     ),
    ("view3d.localview", {"type": 'NUMPAD_SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'MOUSESMARTZOOM', "value": 'ANY'}, None),
    ("view3d.localview_remove_from", {"type": 'NUMPAD_SLASH', "value": 'PRESS', "alt": True}, None),
    ("view3d.localview_remove_from", {"type": 'SLASH', "value": 'PRESS', "alt": True}, None),
    ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
    ("view3d.rotate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
    ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
    ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
    ("view3d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ],
      },
     ),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
    ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("view3d.zoom",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'EQUAL', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELINMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS'},
     {"properties":
      [("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("center", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_view_pie'),
       ],
      },
     ),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "shift": True}, None),
    ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_2', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITDOWN'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_4', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITLEFT'),
       ],
      },
     ),
    ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_6', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_8', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITUP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANDOWN'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANLEFT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANRIGHT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANUP'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("angle", 3.1415927),
       ("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'NORTH'},
     {"properties":
      [("type", 'TOP'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'SOUTH'},
     {"properties":
      [("type", 'BOTTOM'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'EAST'},
     {"properties":
      [("type", 'RIGHT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'WEST'},
     {"properties":
      [("type", 'LEFT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_center_pick", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "alt": True}, None),
    ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
    ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
    ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CW', "value": 'PRESS'},
     {"properties":
      [("angle", 1.5707964),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("angle", -1.5707964),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
     {"properties":
      [("toggle", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("center", True),
       ("object", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "alt": True},
     {"properties":
      [("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True, "alt": True},
     {"properties":
      [("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("view3d.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("view3d.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("view3d.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'TAB', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.use_snap'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_PT_snapping'),
       ("keep_open", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_snap_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'COMMA', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_orientations_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_shading_ex_pie'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("view3d.toggle_xray", {"type": 'Z', "value": 'PRESS', "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'W', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.select_box'),
       ("cycle", True),
       ],
      },
     ),
    ("view3d.rotate", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "alt": True}, None),
    ("view3d.move", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "shift": True, "alt": True}, None),
    ("view3d.zoom", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "ctrl": True, "alt": True}, None),
    ("view3d.view_roll", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "shift": True, "ctrl": True, "alt": True}, None),
    ],
   },
  ),
 ("Grease Pencil Stroke Edit Mode",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("gpencil.interpolate", {"type": 'E', "value": 'PRESS', "ctrl": True}, None),
    ("gpencil.interpolate_sequence", {"type": 'E', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("gpencil.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("gpencil.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("gpencil.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("gpencil.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("gpencil.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("gpencil.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("gpencil.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("gpencil.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
     {"properties":
      [("extend", True),
       ("toggle", True),
       ],
      },
     ),
    ("gpencil.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
    ("gpencil.select",
     {"type": 'L', "value": 'PRESS'},
     {"properties":
      [("extend", True),
       ("entire_strokes", True),
       ],
      },
     ),
    ("gpencil.select",
     {"type": 'L', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ("deselect", True),
       ("entire_strokes", True),
       ],
      },
     ),
    ("gpencil.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
    ("gpencil.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("gpencil.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("gpencil.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("gpencil.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("gpencil.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("gpencil.extrude_move",
     {"type": 'E', "value": 'PRESS'},
     {"properties":
      [("TRANSFORM_OT_translate",
        [("alt_navigation", False),
         ],
        ),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'X', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_edit_gpencil_delete'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'DEL', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_edit_gpencil_delete'),
       ],
      },
     ),
    ("gpencil.dissolve", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
    ("gpencil.dissolve", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
    ("gpencil.blank_frame_add", {"type": 'I', "value": 'PRESS', "shift": True}, None),
    ("wm.call_menu",
     {"type": 'I', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'GPENCIL_MT_gpencil_draw_delete'),
       ],
      },
     ),
    ("gpencil.active_frames_delete_all", {"type": 'DEL', "value": 'PRESS', "shift": True}, None),
    ("gpencil.stroke_separate", {"type": 'P', "value": 'PRESS'}, None),
    ("gpencil.stroke_split", {"type": 'V', "value": 'PRESS'}, None),
    ("gpencil.stroke_join", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
    ("gpencil.stroke_join",
     {"type": 'J', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'JOINCOPY'),
       ],
      },
     ),
    ("gpencil.stroke_cyclical_set",
     {"type": 'F', "value": 'PRESS'},
     {"properties":
      [("type", 'CLOSE'),
       ("geometry", True),
       ],
      },
     ),
    ("gpencil.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("gpencil.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'GPENCIL_MT_snap_pie'),
       ],
      },
     ),
    ("gpencil.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
    ("gpencil.hide",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("gpencil.hide",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("gpencil.selection_opacity_toggle", {"type": 'H', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'Q', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'space_data.overlay.use_gpencil_edit_lines'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'Q', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.use_gpencil_multiedit_line_only'),
       ],
      },
     ),
    ("gpencil.layer_isolate", {"type": 'NUMPAD_ASTERIX', "value": 'PRESS'}, None),
    ("wm.call_menu",
     {"type": 'M', "value": 'PRESS'},
     {"properties":
      [("name", 'GPENCIL_MT_move_to_layer'),
       ],
      },
     ),
    ("gpencil.layer_merge", {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("transform.translate", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG'}, None),
    ("transform.translate",
     {"type": 'G', "value": 'PRESS'},
     {"properties":
      [("alt_navigation", False),
       ],
      },
     ),
    ("transform.rotate",
     {"type": 'R', "value": 'PRESS'},
     {"properties":
      [("alt_navigation", False),
       ],
      },
     ),
    ("transform.resize",
     {"type": 'S', "value": 'PRESS'},
     {"properties":
      [("alt_navigation", False),
       ],
      },
     ),
    ("transform.bend", {"type": 'W', "value": 'PRESS', "shift": True}, None),
    ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("transform.tosphere", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("transform.transform",
     {"type": 'S', "value": 'PRESS', "alt": True},
     {"properties":
      [("mode", 'GPENCIL_SHRINKFATTEN'),
       ],
      },
     ),
    ("transform.transform",
     {"type": 'F', "value": 'PRESS', "shift": True},
     {"properties":
      [("mode", 'GPENCIL_OPACITY'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'O', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_proportional_editing_falloff_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'tool_settings.use_proportional_edit'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'O', "value": 'PRESS', "alt": True},
     {"properties":
      [("data_path", 'tool_settings.use_proportional_connected'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'U', "value": 'PRESS'},
     {"properties":
      [("data_path", 'gpencil_data.use_curve_edit'),
       ],
      },
     ),
    ("object.gpencil_add", {"type": 'A', "value": 'PRESS', "shift": True}, None),
    ("wm.call_menu",
     {"type": 'G', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'GPENCIL_MT_gpencil_vertex_group'),
       ],
      },
     ),
    ("gpencil.selectmode_toggle",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("mode", 0),
       ],
      },
     ),
    ("gpencil.selectmode_toggle",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("mode", 1),
       ],
      },
     ),
    ("gpencil.selectmode_toggle",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("mode", 2),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'Y', "value": 'PRESS'},
     {"properties":
      [("name", 'GPENCIL_MT_layer_active'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'I', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_gpencil_animation'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_gpencil_edit_context_menu'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'APP', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_gpencil_edit_context_menu'),
       ],
      },
     ),
    ],
   },
  ),
 ("Image",
  {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
  {"items":
   [("wm.call_menu_pie",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("name", 'MACHIN3_MT_modes_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("name", 'MACHIN3_MT_modes_pie'),
       ],
      },
     ),
    ("image.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
    ("image.view_all",
     {"type": 'HOME', "value": 'PRESS', "shift": True},
     {"properties":
      [("fit_view", True),
       ],
      },
     ),
    ("image.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("image.view_cursor_center", {"type": 'C', "value": 'PRESS', "shift": True}, None),
    ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
    ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
    ("image.view_pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("image.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("image.view_ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("image.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
    ("image.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
    ("image.view_zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
    ("image.view_zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
    ("image.view_zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
    ("image.view_zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("image.view_zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("image.view_zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("ratio", 8.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("ratio", 4.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("ratio", 2.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_8', "value": 'PRESS', "shift": True},
     {"properties":
      [("ratio", 8.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
     {"properties":
      [("ratio", 4.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_2', "value": 'PRESS', "shift": True},
     {"properties":
      [("ratio", 2.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("ratio", 1.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_2', "value": 'PRESS'},
     {"properties":
      [("ratio", 0.5),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_4', "value": 'PRESS'},
     {"properties":
      [("ratio", 0.25),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_8', "value": 'PRESS'},
     {"properties":
      [("ratio", 0.125),
       ],
      },
     ),
    ("image.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
    ("image.sample", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
    ("image.curves_point_set",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("point", 'BLACK_POINT'),
       ],
      },
     ),
    ("image.curves_point_set",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("point", 'WHITE_POINT'),
       ],
      },
     ),
    ("object.mode_set",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("mode", 'EDIT'),
       ("toggle", True),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 0),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 1),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 2),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'FOUR', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 3),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'FIVE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 4),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'SIX', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 5),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'SEVEN', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 6),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'EIGHT', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 7),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'NINE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 8),
       ],
      },
     ),
    ("image.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("image.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("name", 'IMAGE_MT_mask_context_menu'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'APP', "value": 'PRESS'},
     {"properties":
      [("name", 'IMAGE_MT_mask_context_menu'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'IMAGE_MT_pivot_pie'),
       ],
      },
     ),
    ("image.view_pan", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "shift": True, "alt": True}, None),
    ("image.view_zoom", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "ctrl": True, "alt": True}, None),
    ("paint.sample_color", {"type": 'LEFTMOUSE', "value": 'ANY', "alt": True}, None),
    ],
   },
  ),
 ("Window",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'N', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'TOPBAR_MT_file_new'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'O', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'TOPBAR_MT_file_open_recent'),
       ],
      },
     ),
    ("wm.open_mainfile", {"type": 'O', "value": 'PRESS', "ctrl": True}, None),
    ("wm.save_mainfile", {"type": 'S', "value": 'PRESS', "ctrl": True}, None),
    ("wm.save_as_mainfile", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("wm.save_mainfile",
     {"type": 'S', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("incremental", True),
       ],
      },
     ),
    ("wm.quit_blender", {"type": 'Q', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu",
     {"type": 'Q', "value": 'PRESS'},
     {"properties":
      [("name", 'SCREEN_MT_user_menu'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F1', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'FILE_BROWSER'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F2', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'CLIP_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F3', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'NODE_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F4', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'CONSOLE'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F5', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'VIEW_3D'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F6', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'GRAPH_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F7', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'PROPERTIES'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F8', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'SEQUENCE_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F9', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'OUTLINER'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F10', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'IMAGE_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F11', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'TEXT_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F12', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'DOPESHEET_EDITOR'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'NDOF_BUTTON_MENU', "value": 'PRESS'},
     {"properties":
      [("name", 'USERPREF_PT_ndof_settings'),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS'},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 1.1),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS'},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 0.90909094),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 1.5),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 0.6666667),
       ],
      },
     ),
    ("info.reports_display_update", {"type": 'TIMER_REPORT', "value": 'ANY', "any": True}, None),
    ("wm.doc_view_manual_ui_context", {"type": 'F1', "value": 'PRESS'}, None),
    ("wm.call_panel",
     {"type": 'F2', "value": 'PRESS'},
     {"properties":
      [("name", 'TOPBAR_PT_name'),
       ("keep_open", False),
       ],
      },
     ),
    ("wm.batch_rename", {"type": 'F2', "value": 'PRESS', "ctrl": True}, None),
    ("wm.search_menu", {"type": 'F3', "value": 'PRESS'}, None),
    ("wm.call_menu",
     {"type": 'F4', "value": 'PRESS'},
     {"properties":
      [("name", 'TOPBAR_MT_file_context_menu'),
       ],
      },
     ),
    ("wm.toolbar_fallback_pie", {"type": 'W', "value": 'PRESS', "alt": True}, None),
    ("wm.toolbar_prompt", {"type": 'LEFT_ALT', "value": 'CLICK'}, None),
    ("wm.toolbar_prompt", {"type": 'RIGHT_ALT', "value": 'CLICK'}, None),
    ("wm.search_menu", {"type": 'SPACE', "value": 'PRESS'}, None),
    ("wm.context_toggle",
     {"type": 'D', "value": 'PRESS', "repeat": True},
     {"properties":
      [("data_path", 'scene.tool_settings.use_transform_data_origin'),
       ],
      },
     ),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
