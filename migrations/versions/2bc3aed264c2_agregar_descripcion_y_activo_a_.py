"""Agregar descripcion y activo a Transportadora

Revision ID: 2bc3aed264c2
Revises: 2881243bc6e9
Create Date: 2025-04-06 20:22:10.629925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bc3aed264c2'
down_revision = '2881243bc6e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transportadoras', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descripcion', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('activo', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transportadoras', schema=None) as batch_op:
        batch_op.drop_column('activo')
        batch_op.drop_column('descripcion')

    # ### end Alembic commands ###
